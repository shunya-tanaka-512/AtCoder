import pytest
from ABC083B import get_sum_total


@pytest.mark.parametrize(
    "n, min_sum_digits, max_sum_digits, expected",
    [
        (20, 2, 5, 84),
        (10, 1, 2, 13),
        (100, 4, 16, 4554)
    ],
)
def test_get_sum_total(n, min_sum_digits, max_sum_digits, expected):
    assert get_sum_total(n, min_sum_digits, max_sum_digits) == expected
