from ABC081A import placing_marbles


def test_placing_marbles():
    assert placing_marbles(101) == 2
    assert placing_marbles(000) == 0
    assert placing_marbles(111) == 3
