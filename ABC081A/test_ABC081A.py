import pytest
from ABC081A import get_number_of_marbles


@pytest.mark.parametrize(
    "input_num, expected",
    [
        (101, 2),
        (000, 0),
        (111, 3),
    ],
)
def test_get_number_of_marbles(input_num, expected):
    assert get_number_of_marbles(input_num) == expected
