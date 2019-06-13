from src.utilities.time_utilities import timestr_to_integer

class Lap:
    def __init__(self, hour_of_lap, laptime, number, average_speed):
        self.hour_of_lap = timestr_to_integer(hour_of_lap)
        self.laptime = timestr_to_integer(laptime)
        self.number = int(number)
        self.average_speed = float(average_speed.replace(',', '.'))
