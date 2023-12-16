# サンプルプログラム：メール送信（添付ファイル）
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# 認証の設定：自分の Gmailアドレス と アプリパスワードに書き換える
# ・アプリパスワードは ログインパスワードとは別物です。
# ・アプリパスワードの生成方法は、下記URLを参照してください
# 　https://yuki.world/python-send-gmail-with-app-password/#t_PythonGmail2
GMAIL_ADDRESS = 'xxx@gmail.com'   # Gmailアドレス 
APP_PASSWORD = 'aaaa bbbb ccc dddd'  # アプリパスワード

TO_MAIL = 'xxx@xxx.com' # 送信先メールアドレス（ここも書き換え必須）
MAIL_TITLE = 'メールタイトル（ファイル添付版）'
MAIL_BODY = '''ファイルを添付しました。
ご確認ください！
'''
FILE_NAME = 'cat.jpg'

# メールの設定処理
msg = MIMEMultipart()        # 添付ファイルがある場合は MultiPartにし、 あとから attach する
msg['From'] = GMAIL_ADDRESS  # 送信元メールアドレス
msg['To'] = TO_MAIL          # 送信先メールアドレス
msg['Subject'] = MAIL_TITLE  # メールタイトル
msg.attach(MIMEText(MAIL_BODY))  # メール本文（日本語が含まれるときは MIMEText必須）を attach

# ファイル読込 → メール添付の処理
with open(FILE_NAME, 'rb') as f:
    file = MIMEApplication(f.read())
    
file.add_header('Content-Disposition', 'attachment', filename=FILE_NAME)
msg.attach(file)  # 添付ファイルを attach

# メールの送信処理
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()
smtp.login(GMAIL_ADDRESS, APP_PASSWORD)
smtp.send_message(msg)
smtp.close()

