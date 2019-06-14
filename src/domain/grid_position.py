from src.utilities.time_utilities import integer_to_timestr

class GridPosition:
    def __init__(self, position, pilot, first_position_time):
        self.position = position
        self.pilot = pilot
        self.first_position_time = first_position_time

    def get_full_text(self):
        full_text = [
            f'Position: {self.position}',
            f'Pilot Code: {self.pilot.number}',
            f'Pilot Name: {self.pilot.name}',
            f'Laps Completed: {self.pilot.get_completed_laps()}',
            f'Race Time: {self.pilot.get_elapsed_time()}',
            f'Best Lap: {self.pilot.get_best_lap().number} - {integer_to_timestr(self.pilot.get_best_lap().laptime)}',
            f'Average Speed: {self.pilot.get_average_speed()}',
            f'Time behind first: {integer_to_timestr(self.pilot.get_elapsed_time() - self.first_position_time)}'
        ]

        return '\n'.join(full_text)
