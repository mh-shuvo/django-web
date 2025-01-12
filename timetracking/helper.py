from datetime import date, timedelta

def get_current_week_start_end_date():
    today = date.today()
    # Calculate the start of the week (Saturday)
    start_of_week = today - timedelta(days=(today.weekday() + 2) % 7)
    # Calculate the end of the week (Friday)
    end_of_week = start_of_week + timedelta(days=6)
    return start_of_week, end_of_week