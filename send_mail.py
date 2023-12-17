<<<<<<< HEAD
from Body_make import create_calendar_url, date_format, process_data
=======
import os
>>>>>>> 8cfa5715bd14f19544e329d9810d15b572b28ba4
import smtplib
from email.mime.text import MIMEText
from Body_make import modify_calendar_url, date_format

def send_mail(slots, scales, me):
    to_email = me['email']
    print(to_email)
    GMAIL_ADDRESS = os.getenv('GMAIL_ADDRESS')
    APP_PASSWORD = os.getenv('APP_PASSWORD')

<<<<<<< HEAD
    for scale in scales:
        if 'begin_at' in scale:
            year, month, day, hour, minute = date_format(scale['begin_at'])
            modified_url = create_calendar_url(project_name, year, month, day, hour, minute)
            print("Modified URL:", modified_url)
=======
    # メール本文の初期化
    MAIL_BODY = "メール本文（１行目）\n"

    # scales内のデータをメール本文に組み込む
    url = "https://calendar.google.com/calendar/render?action=TEMPLATE&text=レビュー&details=&dates=20231112T140000/20231112T150000"
    for scale in scales:
        if 'begin_at' in scale:
            new_start_time = date_format(scale['begin_at'])
            modified_url = modify_calendar_url(url, new_start_time)
            MAIL_BODY += f"{new_start_time}: {modified_url}\n"
        
        if 'team' in scale and 'project_gitlab_path' in scale['team']:
            project_path = scale['team']['project_gitlab_path']
            project_name = project_path.split('/')[-1]
            MAIL_BODY += f"プロジェクト名: {project_name}\n"
>>>>>>> 8cfa5715bd14f19544e329d9810d15b572b28ba4

    TO_MAIL = GMAIL_ADDRESS # 送信先メールアドレス（ここも書き換え必須）
    MAIL_TITLE = 'メールタイトル'

    # メールの設定処理
    msg = MIMEText(MAIL_BODY)    # メール本文（日本語が含まれるときは MIMEText必須）
    msg['Subject'] = MAIL_TITLE  # メールタイトル
    msg['From'] = GMAIL_ADDRESS  # 送信元メールアドレス
    msg['To'] = TO_MAIL          # 送信先メールアドレス

<<<<<<< HEAD
            # メールの送信処理
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.starttls()
            smtp.login(GMAIL_ADDRESS, APP_PASSWORD)
            smtp.send_message(msg)
            smtp.close()
        if 
=======
    # メールの送信処理
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(GMAIL_ADDRESS, APP_PASSWORD)
    smtp.send_message(msg)
    smtp.close()
>>>>>>> 8cfa5715bd14f19544e329d9810d15b572b28ba4
