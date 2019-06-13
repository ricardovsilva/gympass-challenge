from operator import attrgetter
from statistics import mean

from src.domain.lap import Lap
from src.utilities.time_utilities import integer_to_timestr

class Pilot:
    def __init__(self, number_and_name):
        self.laps = []
        self.number = int(number_and_name.split(' ')[0])
        self.name = number_and_name.split(' ')[-1]

    def add_lap(self, lap):
        if type(lap) is not Lap:
            raise ValueError('Providen lap must be of type Lap. Check Lap class in file src.domain.lap.py')
        
        self.laps.append(lap)

    def get_best_lap(self):
        return min(self.laps,key=attrgetter('laptime'))

    def get_average_speed(self):
        return round(mean([lap.average_speed for lap in self.laps]), 3)

    def get_elapsed_time(self):
        return integer_to_timestr(sum([lap.laptime for lap in self.laps]))

    def __eq__(self, other):
        return self.number == other.number and self.name == other.name

    