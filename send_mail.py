import os
import smtplib
from email.mime.text import MIMEText
from Body_make import create_calendar_url, date_format

def send_mail(slots, scales, me):
    to_email = me['email']
    print(to_email)
    GMAIL_ADDRESS = os.getenv('GMAIL_ADDRESS')
    APP_PASSWORD = os.getenv('APP_PASSWORD')

    # メール本文の初期化
    MAIL_BODY = ""

    # scales内のデータをメール本文に組み込む
    for scale in scales:
        
        if 'team' in scale and 'project_gitlab_path' in scale['team']:
            project_path = scale['team']['project_gitlab_path']
            project_name = project_path.split('/')[-1]
            MAIL_BODY += f"プロジェクト名: {project_name}\n"

    # メールの内容が空でない場合のみ、メール送信処理を実行
    if MAIL_BODY:
        TO_MAIL = GMAIL_ADDRESS  # 送信先メールアドレス
        MAIL_TITLE = 'メールタイトル'

        # メールの設定処理
        msg = MIMEText(MAIL_BODY)    # メール本文
        msg['Subject'] = MAIL_TITLE  # メールタイトル
        msg['From'] = GMAIL_ADDRESS  # 送信元メールアドレス
        msg['To'] = TO_MAIL          # 送信先メールアドレス

        # メールの送信処理
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(GMAIL_ADDRESS, APP_PASSWORD)
        smtp.send_message(msg)
        smtp.close()
        print("メールを送信しました。")

