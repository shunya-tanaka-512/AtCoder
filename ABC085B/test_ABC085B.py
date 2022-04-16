import pytest
from ABC085B import get_num_of_tiered


@pytest.mark.parametrize(
    "diameter, expected",
    [
        ([10, 8, 8, 6], 3),
        ([15, 15, 15], 1),
        ([50, 30, 50, 100, 50, 80, 30], 4)
    ],
)
def test_get_num_of_tiered(diameter, expected):
    assert get_num_of_tiered(diameter) == expected
