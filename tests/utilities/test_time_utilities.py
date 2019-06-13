from assertpy import assert_that

from src.utilities.time_utilities import timestr_to_integer, integer_to_timestr

class TestTimeUtilities:
    def test__timestr_to_integer__valid_time__should_return_equivalent_integer(self):
        assert_that(timestr_to_integer('1:02.852')).is_equal_to(62852)

    def test__integer_to_timestr__valid_string__should_return_equivalent_timestring(self):
        assert_that(integer_to_timestr(62852)).is_equal_to('1:02.852')