import pytest
from PracticeA import process_data


@pytest.mark.parametrize(
    "param1,param2,param3,param4,expected",
    [(1, 2, 3, "test", (6, "test")), (72, 128, 256, "myonmyon", (456, "myonmyon"))],
)
def test_process_data(param1, param2, param3, param4, expected):
    assert process_data(param1, param2, param3, param4) == (expected)
