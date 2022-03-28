from PracticeA import process_data


def test_process_data():
    assert process_data(1, 2, 3, "test") == (6, "test")
    assert process_data(72, 128, 256, "myonmyon") == (456, "myonmyon")
