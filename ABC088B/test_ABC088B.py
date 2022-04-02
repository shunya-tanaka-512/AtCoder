import pytest
from ABC088B import get_score_diff


@pytest.mark.parametrize(
    "scores, expected",
    [
        ([3, 1], 2),
        ([2, 7, 4], 5),
        ([20, 18, 2, 18], 18)
    ],
)
def test_get_score_diff(scores: list, expected: int):
    assert get_score_diff(scores) == expected
