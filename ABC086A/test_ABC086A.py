from ABC086A import odd_even


def test_odd_even():
    assert odd_even(3, 3) == "Odd"
    assert odd_even(2, 3) == "Even"
    assert odd_even(2, 4) == "Even"
    assert odd_even(1, 10000) == "Even"
