import argparse

from src.domain.race import Race
from src.utilities.time_utilities import integer_to_timestr

parser = argparse.ArgumentParser(description="Processes race log")
parser.add_argument(
    dest="input",
    help="Input file that have the log of race",
    type=argparse.FileType('r')
)

args = parser.parse_args()

with args.input as input_file:
    next(input_file)

    race = Race()
    laps_log = input_file.read().split('\n')
    laps_log = [lap.replace('\t', ' ') for lap in laps_log if lap]

    for lap in laps_log:
        race.add_lap_from_text(lap)

    print('Race summary')
    print(f'Best lap: {race.get_best_lap()}')
    print('\n')

    for grid_position in race.get_grid_positions():
        print(grid_position.get_full_text())
        print('\n')
