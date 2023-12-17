from datetime import datetime, timedelta

def create_google_calendar_link(begin_at, name):
    # Parse the timestamp
    start_time = datetime.fromisoformat(begin_at.replace("Z", "+00:00"))

    # Format start and end times
    start_str = start_time.strftime("%Y%m%dT%H%M00Z")
    end_str = (start_time + timedelta(minutes=45)).strftime("%Y%m%dT%H%M00Z")

    # Construct the URL
    url = f"https://calendar.google.com/calendar/render?action=TEMPLATE&text={name}%E3%81%AE%E3%83%AC%E3%83%93%E3%83%A5%E3%83%BC&details=&dates={start_str}/{end_str}"
    return url

def make_body(slots, scales, me):
    body = "レビュー予約が更新されました。\n\n"
    for scale in scales:
        if isinstance(scale, dict) and 'begin_at' in scale:
            if 'team' in scale and 'project_gitlab_path' in scale['team']:
                gitlab_path = scale['team']['project_gitlab_path'].split('/')[-1]
            else:
                gitlab_path = "unknown"

            try:
                timestamp = datetime.fromisoformat(scale['begin_at'].replace("Z", "+00:00"))
                formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M")
                calendar_link = create_google_calendar_link(scale['begin_at'], gitlab_path)
            except ValueError:
                formatted_timestamp = "unknown"
                calendar_link = "unavailable"


            body += f"- {formatted_timestamp}~\n課題名: {gitlab_path}\nGoogleカレンダーに追加: {calendar_link}\n\n"
        else:
            body += "- unknown data\n\n"

    return body
