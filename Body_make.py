import datetime
from datetime import timedelta
import urllib.parse
import pytz

def modify_calendar_url(url, new_start_time):
    # パスワードの解析
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)
    original_dates = query_params['dates'][0]  # この行を追加

    new_start_datetime = datetime.datetime.strptime(new_start_time, "%Y%m%dT%H%M%S")

    # 45分後を終了時刻とする
    new_end_datetime = new_start_datetime + datetime.timedelta(minutes=45)

    new_end_time = new_end_datetime.strftime("%Y%m%dT%H%M%S")

    new_dates = f"{new_start_time}/{new_end_time}"
    new_url = url.replace(original_dates, new_dates)

    return new_url

from dateutil import parser

def date_format(iso_datetime):
    # dateutil.parserを使用してUTCのdatetimeオブジェクトに変換
    utc_datetime = parser.parse(iso_datetime)

    # 日本時間に変換（UTC+9時間）
    japan_timezone = pytz.timezone('Asia/Tokyo')
    japan_datetime = utc_datetime.astimezone(japan_timezone)

    # 日本時間を指定のフォーマットに変換
    formatted_japan_datetime = japan_datetime.strftime("%Y%m%d%H%M")

    return formatted_japan_datetime


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