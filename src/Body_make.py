import datetime
import urllib.parse

def modify_calendar_url(url, new_start_time):
    # パスワードの解析
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)

    new_start_datetime = datetime.datetime.strptime(new_start_time, "%Y%m%dT%H%M%S")

    # 45分後を終了時刻とする
    new_end_datetime = new_start_datetime + datetime.timedelta(minutes=45)

    new_end_time = new_end_datetime.strftime("%Y%m%dT%H%M%S")

    new_dates = f"{new_start_time}/{new_end_time}"
    new_url = url.replace(original_dates, new_dates)

    return new_url

def