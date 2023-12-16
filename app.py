from flask import Flask, request, redirect, session, render_template, jsonify
import requests
from send_mail import send_mail
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = 'http://127.0.0.1:5000/callback'
AUTHORIZE_URL = 'https://api.intra.42.fr/oauth/authorize'
TOKEN_URL = 'https://api.intra.42.fr/oauth/token'

@app.route('/')
def home():
    return render_template( "index.html" )
@app.route('/auth')
def auth():
    return redirect(
        f"{AUTHORIZE_URL}?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
        f"&response_type=code&scope=public projects&state=random_state_string"
    )

@app.route('/callback')
def callback():
    code = request.args.get('code')
    state = request.args.get('state')

    if state != 'random_state_string':
        return 'State mismatch', 400

    token_response = requests.post(TOKEN_URL, data={
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
        'redirect_uri': REDIRECT_URI,
    })

    session['access_token'] = token_response.json().get('access_token')
    return redirect('/profile')

@app.route('/profile')
def profile():
    headers = {'Authorization': f"Bearer {session.get('access_token')}"}
    me = requests.get('https://api.intra.42.fr/v2/me', headers=headers)
    slots = requests.get('https://api.intra.42.fr/v2/me/slots', headers=headers)
    scale_teams = requests.get('https://api.intra.42.fr/v2/me/scale_teams', headers=headers)
    corrected = requests.get('https://api.intra.42.fr/v2/me/scale_teams/as_corrected', headers=headers)
    corrector = requests.get('https://api.intra.42.fr/v2/me/scale_teams/as_corrector', headers=headers)
    send_mail(slots.json(), scale_teams.json(), me.json())
    return render_template( "profile.html", corrected=corrected.json(), corrector=corrector.json(),scale_teams=scale_teams.json(), slots=slots.json(), me=me.json())

@app.route('/send_mail', methods=['POST'])
def send():
    headers = {'Authorization': f"Bearer {session.get('access_token')}"}
    me = requests.get('https://api.intra.42.fr/v2/me', headers=headers)
    slots = requests.get('https://api.intra.42.fr/v2/me/slots', headers=headers)
    scale_teams = requests.get('https://api.intra.42.fr/v2/me/scale_teams', headers=headers)
    send_mail(slots.json(), scale_teams.json(), me.json())
    return jsonify({"message": "Email sent successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    # app.run(debug=True, port=8888)
