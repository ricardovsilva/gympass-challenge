from src.domain.lap import Lap
from src.domain.pilot import Pilot
from src.utilities.time_utilities import integer_to_timestr

class Race:
    def __init__(self):
        self.pilots = []

    def add_lap_from_text(self, lap_text):
        HOUR_INDEX = 0
        PILOT_NUMBER_INDEX = 1
        PILOT_NAME_INDEX = 3
        LAP_NUMBER_INDEX = 4
        LAPTIME_INDEX = 5
        AVERAGE_SPEED_INDEX = 6

        lap_elements = list(filter(None, lap_text.split(' ')))
        lap = Lap(lap_elements[HOUR_INDEX], lap_elements[LAPTIME_INDEX], lap_elements[LAP_NUMBER_INDEX], lap_elements[AVERAGE_SPEED_INDEX])

        pilot = next((p for p in self.pilots if p.number == lap_elements[PILOT_NUMBER_INDEX] and p.name == lap_elements[PILOT_NAME_INDEX]), None)
        if not pilot:
            pilot = Pilot([lap_elements[PILOT_NUMBER_INDEX], lap_elements[PILOT_NAME_INDEX]])
            self.pilots.append(pilot)
        
        pilot.add_lap(lap)


    def get_grid_positions(self):
        pilots_ordered = sorted(self.pilots, key=lambda pilot: pilot.get_elapsed_time())
        return pilots_ordered

    def get_best_lap(self):
        best_lap_pilot = sorted(self.pilots, key=lambda pilot: pilot.get_best_lap().laptime)[0]
        return f"{best_lap_pilot.name} - {integer_to_timestr(best_lap_pilot.get_best_lap().laptime)}"