import os
import smtplib
from email.mime.text import MIMEText
# from Body_make import create_calendar_url, date_format
from make_body import make_body

def send_mail(slots, scales, me):
    to_email = me['email']
    print(to_email)
    GMAIL_ADDRESS = os.getenv('GMAIL_ADDRESS')
    APP_PASSWORD = os.getenv('APP_PASSWORD')

    # メール本文の初期化
    # MAIL_BODY = ""

    # for scale in scales:
    #     if 'team' in scale and 'project_gitlab_path' in scale['team']:
    #         project_path = scale['team']['project_gitlab_path']
    #         project_name = project_path.split('/')[-1]
    #         MAIL_BODY += f"プロジェクト名: {project_name}\n"

    #     if 'begin_at' in scale:
    #         year, month, day, hour, minute = date_format(scale['begin_at'])
    #         modified_url = create_calendar_url(project_name, year, month, day, hour, minute)
    #         MAIL_BODY += f"{year}/{month}/{day} {hour}:{minute}: {modified_url}\n"

    if len(scales) != 0:
        MAIL_BODY = make_body(slots, scales, me)
        TO_MAIL = GMAIL_ADDRESS
        MAIL_TITLE = 'メールタイトル'

        msg = MIMEText(MAIL_BODY)
        msg['Subject'] = MAIL_TITLE
        msg['From'] = GMAIL_ADDRESS
        msg['To'] = TO_MAIL

        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(GMAIL_ADDRESS, APP_PASSWORD)
        smtp.send_message(msg)
        smtp.close()

        print("メールを送信しました。")
