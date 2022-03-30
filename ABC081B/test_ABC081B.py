import pytest
from ABC081B import get_times_dividable_in_2


@pytest.mark.parametrize(
    "int_val_tuple, expected",
    [
        ((8, 12, 40), 2),
        ((5, 6, 8, 10), 0),
        ((382253568, 723152896, 37802240, 379425024, 404894720, 471526144), 8),
    ],
)
def test_get_times_dividable_in_2(int_val_tuple, expected):
    assert get_times_dividable_in_2(int_val_tuple) == expected
