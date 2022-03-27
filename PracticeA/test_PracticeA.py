from PracticeA import data_processing


def test_data_processing():
    assert data_processing(1, 2, 3, "test") == (6, "test")
    assert data_processing(72, 128, 256, "myonmyon") == (456, "myonmyon")
