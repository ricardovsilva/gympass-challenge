from operator import attrgetter
from statistics import mean

from src.domain.lap import Lap

class Pilot:
    def __init__(self, number_and_name):
        self.laps = []
        if type(number_and_name) is str:
            self.number = number_and_name.split(' ')[0]
            self.name = number_and_name.split(' ')[-1]
        elif type(number_and_name) is list:
            self.number, self.name = number_and_name
        else:
            raise ValueError('number_and_name must be a string or a list')

    def add_lap(self, lap):
        if type(lap) is not Lap:
            raise ValueError('Providen lap must be of type Lap. Check Lap class in file src.domain.lap.py')
        
        self.laps.append(lap)

    def get_best_lap(self):
        return min(self.laps,key=attrgetter('laptime'))

    def get_average_speed(self):
        return round(mean([lap.average_speed for lap in self.laps]), 3)

    def get_elapsed_time(self):
        return self.laps[-1].hour_of_lap - self.laps[0].begin_of_lap

    def get_completed_laps(self):
        return len(self.laps)

    def __eq__(self, other):
        return self.number == other.number and self.name == other.name

    