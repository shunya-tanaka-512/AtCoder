import pytest
from ABC087B import get_pattern_select_coins


@pytest.mark.parametrize(
    "yen500_num, yen100_num, yen50_num, yen_sum, expected",
    [
        (2, 2, 2, 100, 2),
        (5, 1, 0, 150, 0),
        (30, 40, 50, 6000, 213)
    ],
)
def test_get_pattern_select_coins(yen500_num, yen100_num, yen50_num, yen_sum, expected):
    assert get_pattern_select_coins(yen500_num, yen100_num, yen50_num, yen_sum) == expected
