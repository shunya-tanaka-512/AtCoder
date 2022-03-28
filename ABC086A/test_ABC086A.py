from ABC086A import judge_odd_or_even


def test_judge_odd_or_even():
    assert judge_odd_or_even(3, 3) == "Odd"
    assert judge_odd_or_even(2, 3) == "Even"
    assert judge_odd_or_even(2, 4) == "Even"
    assert judge_odd_or_even(1, 10000) == "Even"
