# サンプルプログラム：メール送信（通常）
import smtplib
from email.mime.text import MIMEText

# 認証の設定：自分の Gmailアドレス と アプリパスワードに書き換える
# ・アプリパスワードは ログインパスワードとは別物です。
# ・アプリパスワードの生成方法は、下記URLを参照してください
# 　https://yuki.world/python-send-gmail-with-app-password/#t_PythonGmail2
GMAIL_ADDRESS = 'xxx@gmail.com'   # Gmailアドレス 
APP_PASSWORD = 'aaaa bbbb cccc dddd'  # アプリパスワード

TO_MAIL = 'xxx@xxx.com' # 送信先メールアドレス（ここも書き換え必須）
MAIL_TITLE = 'メールタイトル'
MAIL_BODY = '''メール本文（１行目）
メール本文（２行目）
メール本文（３行目）
'''

# メールの設定処理
msg = MIMEText(MAIL_BODY)    # メール本文（日本語が含まれるときは MIMEText必須）
msg['Subject'] = MAIL_TITLE  # メールタイトル
msg['From'] = GMAIL_ADDRESS  # 送信元メールアドレス
msg['To'] = TO_MAIL          # 送信先メールアドレス

# メールの送信処理
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()
smtp.login(GMAIL_ADDRESS, APP_PASSWORD)
smtp.send_message(msg)
smtp.close()