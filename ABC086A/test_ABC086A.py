import pytest
from ABC086A import judge_odd_or_even


@pytest.mark.parametrize(
    "param1,param2,expected",
    [(3, 3, "Odd"), (2, 3, "Even"), (2, 4, "Even"), (1, 10000, "Even")],
)
def test_judge_odd_or_even(param1, param2, expected):
    assert judge_odd_or_even(param1, param2) == expected
