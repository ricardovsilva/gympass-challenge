def timestr_to_integer(time):
    time_parts = time.split(':')
    time_have_hours = time.count(':') == 2

    hours = int(time_parts[0]) if time_have_hours else 0
    minutes = int(time_parts[1 if time_have_hours else 0])
    remaining = time_parts[-1].split('.')
    seconds = int(remaining[0])
    milliseconds = int(remaining[-1])

    return ((hours * 3600 + minutes * 60 + seconds) * 1000) + milliseconds

def integer_to_timestr(integer_time):
    milliseconds = integer_time % 1000
    remaining_seconds = (integer_time - milliseconds)/1000
    seconds = remaining_seconds % 60
    remaining_minutes = (remaining_seconds - seconds)/60
    minutes = remaining_minutes % 60
    remaining_minutes = remaining_minutes - minutes
    hours = remaining_minutes/60

    result = f"{int(minutes)}:{'%02d' % seconds}.{'%03d' % milliseconds}"
    return f"{int(hours)}:{result}" if hours else result