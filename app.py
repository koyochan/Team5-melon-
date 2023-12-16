from flask import Flask, request, redirect, session, render_template
import requests
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
        f"&response_type=code&scope=public&state=random_state_string"
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
    response = requests.get('https://api.intra.42.fr/v2/me/scale_teams/as_corrected', headers=headers)
    return response.json()

@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    # Redirect to home page or a different page
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    # app.run(debug=True, port=8888)
