from ABC081B import get_times_dividable_in_2


def test_get_times_dividable_in_2():
    assert (
        get_times_dividable_in_2(
            [
                8,
                12,
                40,
            ]
        )
        == 2
    )
    assert (
        get_times_dividable_in_2(
            [
                5,
                6,
                8,
                10,
            ]
        )
        == 0
    )
    assert (
        get_times_dividable_in_2(
            [382253568, 723152896, 37802240, 379425024, 404894720, 471526144]
        )
        == 8
    )
