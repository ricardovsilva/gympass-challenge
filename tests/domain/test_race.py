from assertpy import assert_that
import pytest

from src.domain.pilot import Pilot
from src.domain.race import Race

class TestRace:
    @pytest.fixture
    def race(self):
        return Race()

    @pytest.fixture
    def complete_race(self):
        complete_race = Race()
        complete_race.add_lap_from_text('23:49:08.277 038 – F.MASSA 1 1:02.852 44,275')
        complete_race.add_lap_from_text('23:49:10.858 033 – R.BARRICHELLO 1 1:04.352 43,243')
        complete_race.add_lap_from_text('23:49:11.075 002 – K.RAIKKONEN 1 1:04.108 43,408')
        complete_race.add_lap_from_text('23:49:12.667 023 – M.WEBBER 1 1:04.414 43,202')
        complete_race.add_lap_from_text('23:49:30.976 015 – F.ALONSO 1 1:18.456 35,47')
        complete_race.add_lap_from_text('23:50:11.447 038 – F.MASSA 2 1:03.170 44,053')
        complete_race.add_lap_from_text('23:50:14.860 033 – R.BARRICHELLO 2 1:04.002 43,48')
        complete_race.add_lap_from_text('23:50:15.057 002 – K.RAIKKONEN 2 1:03.982 43,493')
        complete_race.add_lap_from_text('23:50:17.472 023 – M.WEBBER 2 1:04.805 42,941')
        complete_race.add_lap_from_text('23:50:37.987 015 – F.ALONSO 2 1:07.011 41,528')
        complete_race.add_lap_from_text('23:51:14.216 038 – F.MASSA 3 1:02.769 44,334')
        complete_race.add_lap_from_text('23:51:18.576 033 – R.BARRICHELLO 3 1:03.716 43,675')
        complete_race.add_lap_from_text('23:51:19.044 002 – K.RAIKKONEN 3 1:03.987 43,49')
        complete_race.add_lap_from_text('23:51:21.759 023 – M.WEBBER 3 1:04.287 43,287')
        complete_race.add_lap_from_text('23:51:46.691 015 – F.ALONSO 3 1:08.704 40,504')
        complete_race.add_lap_from_text('23:52:01.796 011 – S.VETTEL 1 3:31.315 13,169')
        complete_race.add_lap_from_text('23:52:17.003 038 – F.MASSA 4 1:02.787 44,321')
        complete_race.add_lap_from_text('23:52:22.586 033 – R.BARRICHELLO 4 1:04.010 43,474')
        complete_race.add_lap_from_text('23:52:22.120 002 – K.RAIKKONEN 4 1:03.076 44,118')
        complete_race.add_lap_from_text('23:52:25.975 023 – M.WEBBER 4 1:04.216 43,335')
        complete_race.add_lap_from_text('23:53:06.741 015 – F.ALONSO 4 1:20.050 34,763')
        complete_race.add_lap_from_text('23:53:39.660 011 – S.VETTEL 2 1:37.864 28,435')
        complete_race.add_lap_from_text('23:54:57.757 011 – S.VETTEL 3 1:18.097 35,633')
        return complete_race
 
    def test__add_lap_from_text__lap_with_new_pilot__should_add_pilot(self, race):
        race.add_lap_from_text('23:49:08.277 038 – F.MASSA 1 1:02.852 44,275')
        assert_that(race.pilots).is_length(1)
        assert_that(race.pilots[0].laps).is_length(1)

    def test__add_lap_from_text__lap_of_pilot_already_added__should_keep_pilot_and_add_lap(self, race):
        race.add_lap_from_text('23:49:08.277 038 – F.MASSA 1 1:02.852 44,275')
        race.add_lap_from_text('23:50:11.447 038 – F.MASSA 2 1:03.170 44,053')
        assert_that(race.pilots).is_length(1)
        assert_that(race.pilots[0].laps).is_length(2)

    def test__add_lap_from_text__laps_of_two_pilots__should_add_both_pilots(self, race):
        race.add_lap_from_text('23:49:08.277 038 – F.MASSA 1 1:02.852 44,275')
        race.add_lap_from_text('23:49:10.858 033 – R.BARRICHELLO 1 1:04.352 43,243')
        assert_that(race.pilots).is_length(2)
        assert_that(race.pilots[0].laps).is_length(1)
        assert_that(race.pilots[1].laps).is_length(1)

    def test__get_grid_positions__with_complete_race__should_return_f_massa_as_first(self, complete_race):
        target = complete_race.get_grid_positions()[0]
        assert_that(target).has_number('038')
        assert_that(target).has_name('F.MASSA')

    def test__get_grid_positions__with_complete_race__should_return_s_vettel_massa_as_last(self, complete_race):
        target = complete_race.get_grid_positions()[-1]
        assert_that(target).has_number('011')
        assert_that(target).has_name('S.VETTEL')

    def test__get_grid_positions__with_complete_race__should_have_six_pilots(self, complete_race):
        assert_that(complete_race.get_grid_positions()).is_length(6)

    def test__get_grid_positions__with_complete_race__first_position_should_have_four_laps_completed(self, complete_race):
        assert_that(complete_race.get_grid_positions()[0].laps).is_length(4)

    def test__get_grid_positions__with_complete_race__last_position_should_have_three_laps_completed(self, complete_race):
        assert_that(complete_race.get_grid_positions()[-1].laps).is_length(3)

    