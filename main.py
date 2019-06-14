import argparse

from src.domain.race import Race
from src.utilities.time_utilities import integer_to_timestr

parser = argparse.ArgumentParser(description="Processes race log")
parser.add_argument('-f', '--input', dest="input", help="Input file that have the log of race", type=argparse.FileType('r'))

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

    for i, pilot in enumerate(race.get_grid_positions()):
        position = i + 1
        print(f'Position: {position}')
        print(f'Pilot Code: {pilot.number}')
        print(f'Pilot Name: {pilot.name}')
        print(f'Laps Completed: {len(pilot.laps)}')
        print(f'Race Time: {pilot.get_elapsed_time()}')
        print(f'Best Lap: {integer_to_timestr(pilot.get_best_lap().laptime)}')
        print(f'Average Speed: {pilot.get_average_speed()}')
        print('\n')



