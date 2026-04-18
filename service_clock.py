from datetime import datetime
import pytz

def metro_service_status():

    india = pytz.timezone("Asia/Kolkata")
    now = datetime.now(india)

    start_time = now.replace(hour=6, minute=0, second=0, microsecond=0)
    end_time = now.replace(hour=23, minute=0, second=0, microsecond=0)

    if start_time <= now <= end_time:
        return True
    else:
        return False
