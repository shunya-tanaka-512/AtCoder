from ABC087B import get_pattern_select_coins


def test_get_pattern_select_coins():
    assert get_pattern_select_coins(2, 2, 2, 100) == 2
    assert get_pattern_select_coins(5, 1, 0, 150) == 0
    assert get_pattern_select_coins(30, 40, 50, 6000) == 213
