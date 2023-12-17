import datetime
from datetime import timedelta
import urllib.parse
import pytz

def create_calendar_url(project_name, year, month, day, hour, minute):
    # 開始日時を設定
    start_datetime = datetime(year, month, day, hour, minute)

    # 45分後の終了日時を計算
    end_datetime = start_datetime + timedelta(minutes=45)

    # 日付と時刻をフォーマット
    start_str = start_datetime.strftime("%Y%m%dT%H%M00")
    end_str = end_datetime.strftime("%Y%m%dT%H%M00")

    # URLを生成
    url = f"https://calendar.google.com/calendar/render?action=TEMPLATE&text={project_name}&details=&dates={start_str}/{end_str}"
    return url
    

from dateutil import parser

def date_format(iso_datetime):
    # dateutil.parserを使用してUTCのdatetimeオブジェクトに変換
    utc_datetime = parser.parse(iso_datetime)

    # 日本時間に変換（UTC+9時間）
    japan_timezone = pytz.timezone('Asia/Tokyo')
    japan_datetime = utc_datetime.astimezone(japan_timezone)

    # 日本時間を年、月、日、時、分に分割
    year = japan_datetime.year
    month = japan_datetime.month
    day = japan_datetime.day
    hour = japan_datetime.hour
    minute = japan_datetime.minute

    return year, month, day, hour, minute


def process_data(sample_data):
    extracted_project_names = []
    for item in sample_data:
        project_gitlab_path = item.get('team', {}).get('project_gitlab_path', '')
        if project_gitlab_path:
            project_name = project_gitlab_path.split('/')[-1]
            extracted_project_names.append(project_name)

    # ここで他の処理を追加 (例: modify_calendar_url, date_formatなど)
    # 例: URL変更や日付フォーマット処理など

    return extracted_project_names