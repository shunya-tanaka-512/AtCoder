import pytest
from ABC049C import judge_str_match


@pytest.mark.parametrize(
    "character_str, expected",
    [
        ("erasedream", "YES"),
        ("dreameraser", "YES"),
        ("dreamerer", "NO")
    ],
)
def test_judge_str_match(character_str: str, expected: str):
    assert judge_str_match(character_str) == expected
