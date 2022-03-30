import pytest
from PracticeA import process_data


@pytest.mark.parametrize(
    "a, b, c, s, expected",
    [
        (1, 2, 3, "test", (6, "test")),
        (72, 128, 256, "myonmyon", (456, "myonmyon"))
    ],
)
def test_process_data(a, b, c, s, expected):
    assert process_data(a, b, c, s) == (expected)
