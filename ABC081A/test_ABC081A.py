from ABC081A import get_number_of_marbles


def test_get_number_of_marbles():
    assert get_number_of_marbles(101) == 2
    assert get_number_of_marbles(000) == 0
    assert get_number_of_marbles(111) == 3
