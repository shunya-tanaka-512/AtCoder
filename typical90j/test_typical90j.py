import pytest
from typical90j import get_score_totals


@pytest.mark.parametrize(
    "n, classes_and_scores, q, id_nums, expected",
    [
        (
            7,
            [[1, 72], [2, 78], [2, 94], [1, 23], [2, 89], [1, 40], [1, 75]],
            1,
            [[2, 6]],
            [[63, 261]]

        ),
        (
            7,
            [[1, 72], [2, 78], [2, 94], [1, 23], [2, 89], [1, 40], [1, 75]],
            10,
            [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [1, 5], [2, 6], [3, 7], [1, 6], [2, 7]],
            [[72, 172], [23, 172], [23, 183], [63, 89], [115, 89], [95, 261], [63, 261], [138, 183], [135, 261], [138, 261]]
        ),
        (
            1,
            [[1, 100]],
            3,
            [[1, 1], [1, 1], [1, 1]],
            [[100, 0], [100, 0], [100, 0]]
        ),
    ],
)
def test_get_score_totals(n: int, classes_and_scores: list, q: int, id_nums: list, expected: list):
    assert get_score_totals(n, classes_and_scores, q, id_nums) == expected
