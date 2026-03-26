from datetime import datetime, timedelta


def get_print_time(seconds):
    """
    Convert seconds to HH:MM:SS format.
    """
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"


def calculate_work_hours(start_time, end_time):
    """
    Calculate work hours given start and end datetime strings in HH:MM:SS format.
    """
    start = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    duration = end - start
    return duration.total_seconds() / 3600  # Return hours


def add_days(start_date, days):
    """
    Add a number of days to a date string in YYYY-MM-DD format.
    """
    date = datetime.strptime(start_date, '%Y-%m-%d')
    new_date = date + timedelta(days=days)
    return new_date.strftime('%Y-%m-%d')


def subtract_days(start_date, days):
    """
    Subtract a number of days from a date string in YYYY-MM-DD format.
    """
    date = datetime.strptime(start_date, '%Y-%m-%d')
    new_date = date - timedelta(days=days)
    return new_date.strftime('%Y-%m-%d')

# Example usage:
if __name__ == '__main__':
    print(get_print_time(3661))  # Should print 01:01:01
    print(calculate_work_hours('2026-03-26 09:00:00', '2026-03-26 17:00:00'))  # Should print 8.0
    print(add_days('2026-03-26', 5))  # Should print 2026-03-31
    print(subtract_days('2026-03-26', 5))  # Should print 2026-03-21
