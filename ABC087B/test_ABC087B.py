import pytest
from ABC087B import get_pattern_select_coins


@pytest.mark.parametrize(
    "param1,param2,param3,param4,expected",
    [(2, 2, 2, 100, 2), (5, 1, 0, 150, 0), (30, 40, 50, 6000, 213)],
)
def test_get_pattern_select_coins(param1, param2, param3, param4, expected):
    assert get_pattern_select_coins(param1, param2, param3, param4) == expected
