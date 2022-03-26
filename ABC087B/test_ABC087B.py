from ABC087B import coins_count


def test_coins_count():
    assert coins_count(2, 2, 2, 100) == 2
    assert coins_count(5, 1, 0, 150) == 0
    assert coins_count(30, 40, 50, 6000) == 213
