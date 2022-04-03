import pytest
from ABC086C import judge_possible_or_impossible


@pytest.mark.parametrize(
    "time_point_list, expected",
    [
        ([[3, 1, 2], [6, 1, 1]], "Yes"),
        ([[2, 100, 100]], "No"),
        ([[5, 1, 1], [100, 1, 1]], "No")
    ],
)
def test_judge_possible_or_impossible(time_point_list: list, expected: str):
    assert judge_possible_or_impossible(time_point_list) == expected
