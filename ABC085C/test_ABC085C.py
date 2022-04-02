import pytest
from ABC085C import get_bill_combination


@pytest.mark.parametrize(
    "num_of_bills, sum_total, expected",
    [
        (9, 45000, [4, 0, 5]),
        (20, 196000, [-1, -1, -1]),
        (2000, 20000000, [2000, 0, 0])
    ],
)
def test_get_bill_combination(num_of_bills: int, sum_total: int, expected: list):
    assert get_bill_combination(num_of_bills, sum_total) == expected
