# time_conversion.py

def convert_to_12_hour_format(hour):
    """Converts 24-hour time to 12-hour time."""
    if 0 <= hour < 12:
        return f"{hour if hour != 0 else 12} AM"
    elif 12 <= hour < 24:
        return f"{hour - 12 if hour != 12 else 12} PM"
    else:
        return "Invalid hour"
