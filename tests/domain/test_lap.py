from assertpy import assert_that
import pytest

from src.domain.lap import Lap

class TestLap:
    @pytest.fixture
    def lap(self):
        return Lap(**{
            'hour_of_lap': '23:49:08.277',
            'number': '1',
            'laptime': '1:02.852',
            'average_speed': '44,275'
        })

    def test__init__given_string_hour__it_should_be_of_type_int(self, lap):
        assert_that(lap.hour_of_lap).is_type_of(int)

    def test__init__given_string_number__it_should_be_of_type_int(self, lap):
        assert_that(lap.number).is_type_of(int)

    def test__init__given_laptime_string__it_should_be_of_type_int(self, lap):
        assert_that(lap.laptime).is_type_of(int)

    def test__init__given_laptime_string__it_should_be_represented_as_milliseconds(self, lap):
        assert_that(lap).has_laptime(62852)

    def test__init__given_average_speed_string__it_should_be_of_type_float(self, lap):
        assert_that(lap.average_speed).is_type_of(float)
        