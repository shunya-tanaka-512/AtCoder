import pytest
from ABC083B import get_sum_total


@pytest.mark.parametrize(
    "int_num, digit_sum_a, digit_sum_b, expected",
    [
        (20, 2, 5, 84),
        (10, 1, 2, 13),
        (100, 4, 16, 4554)
    ],
)
def test_get_sum_total(int_num, digit_sum_a, digit_sum_b, expected):
    assert get_sum_total(int_num, digit_sum_a, digit_sum_b) == expected
