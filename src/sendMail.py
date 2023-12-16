# サンプルプログラム：メール送信（通常）
import smtplib
from email.mime.text import MIMEText
from Body_make import modify_calendar_url

# 認証の設定：自分の Gmailアドレス と アプリパスワードに書き換える
# ・アプリパスワードは ログインパスワードとは別物です。
# ・アプリパスワードの生成方法は、下記URLを参照してください
# 　https://yuki.world/python-send-gmail-with-app-password/#t_PythonGmail2
GMAIL_ADDRESS = 'kkobayashi12356@gmail.com'   # Gmailアドレス 
APP_PASSWORD = 'musl szie muey zien'  # アプリパスワード

# data整形


# data整形(project名)


url = "https://calendar.google.com/calendar/render?action=TEMPLATE&text=レビュー&details=&dates=20231112T140000/20231112T150000"
new_start_time = "22000101T010000"
modified_url = modify_calendar_url(url, new_start_time)
print("Modified URL:", modified_url)

TO_MAIL = 'kkobayashi12356@gmail.com' # 送信先メールアドレス（ここも書き換え必須）
MAIL_TITLE = 'メールタイトル'
MAIL_BODY =  f'''メール本文（１行目）{modified_url}
メール本文の続き...'''

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