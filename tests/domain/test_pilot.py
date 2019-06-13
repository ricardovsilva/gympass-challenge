from assertpy import assert_that
import pytest

from src.domain.pilot import Pilot
from src.domain.lap import Lap

class TestPilot:
    @pytest.fixture
    def pilot(self):
        return Pilot('999 - F.FOO')

    def test__init__given_string_with_number_and_name__should_set_number_and_name(self, pilot):
        assert_that(pilot).has_number(999)
        assert_that(pilot).has_name('F.FOO')

    def test__init__given_two_pilots_with_same_number_and_name__they_should_be_equals(self, pilot):
        assert_that(pilot).is_equal_to(Pilot('999 - F.FOO'))

    def test__add_lap__parameter_not_of_type_lap__should_raise_value_error(self, pilot):
        assert_that(pilot.add_lap).raises(ValueError).when_called_with('foo')

    def test__add_lap__valid_lap__should_add_lap(self, pilot):
        target = Lap(**{
            'hour_of_lap': '23:49:08.277',
            'number': '1',
            'laptime': '1:02.852',
            'average_speed': '44,275'
        })
        pilot.add_lap(target)
        assert_that(pilot.laps).is_length(1)
        assert_that(pilot.laps[-1]).is_equal_to(target)

    def test__get_best_lap__should_return_lap_with_lower_laptime(self, pilot):
        pilot.add_lap(Lap('23:49:08.277', '1:02.852', '1', '44,275'))
        pilot.add_lap(Lap('23:50:11.447', '1:03.170', '2', '44,053'))
        pilot.add_lap(Lap('23:51:14.216', '1:02.769', '3', '44,334'))
        pilot.add_lap(Lap('23:51:14.216', '1:02.787', '4', '44,321'))

        assert_that(pilot.get_best_lap()).has_number(3)

    def test__get_average_speed__should_return_average_speed_of_all_laps(self, pilot):
        pilot.add_lap(Lap('23:49:10.858', '1:04.352', '1', '43,243'))
        pilot.add_lap(Lap('23:50:14.860', '1:04.002', '2', '43,48'))
        pilot.add_lap(Lap('23:51:18.576', '1:03.716', '3', '43,675'))
        pilot.add_lap(Lap('23:52:22.586', '1:04.010', '4', '43,474'))

        assert_that(pilot.get_average_speed()).is_equal_to(43.468)
    
    def test__get_elapsed_time__should_return_sum_of_laptimes(self, pilot):
        target = [
            Lap('23:49:08.277', '1:02.852', '1', '44,275'),
            Lap('23:50:11.447', '1:03.170', '2', '44,053'),
            Lap('23:51:14.216', '1:02.769', '3', '44,334'),
            Lap('23:51:14.216', '1:02.787', '4', '44,321')
        ]

        [pilot.add_lap(lap) for lap in target]
        assert_that(pilot.get_elapsed_time()).is_equal_to('4:11.578')

