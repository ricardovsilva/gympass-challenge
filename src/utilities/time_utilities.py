def timestr_to_integer(time):
    time_parts = time.split(':')
    minutes = int(time_parts[0])
    remaining = time_parts[-1].split('.')
    seconds = int(remaining[0])
    milliseconds = int(remaining[-1])

    return (((minutes * 60) + seconds) * 1000) + milliseconds

def integer_to_timestr(integer_time):
    milliseconds = integer_time % 1000
    remaining = (integer_time - milliseconds)/1000
    seconds = remaining % 60
    minutes = (remaining - seconds)/60

    return f"{int(minutes)}:{'%02d' % seconds}.{'%03d' % milliseconds}"