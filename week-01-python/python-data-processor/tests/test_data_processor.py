import pytest
from data_processor import DataProcessor , process_age
from frequency import count_frequency
def test_minimum():
    processor = DataProcessor([10, 20, 5])
    sonuc =processor.minimum()
    assert sonuc == 5

def test_minimum_empty_data():
    processor = DataProcessor([])
    sonuc =processor.minimum()
    assert sonuc is None

def test_minimum_with_none():
    processor = DataProcessor([10, None, 5, 20])

    sonuc = processor.minimum()

    assert sonuc == 5

def test_duplicates():
    processor = DataProcessor([10, 10, 10, 20, 20, 30])

    sonuc = processor.duplicates()

    assert sonuc == [10, 20]


def test_count_frequency():
    numbers = [10, 20, 10, 30, 20, 10]

    result = count_frequency(numbers)

    assert result == {10: 3, 20: 2, 30: 1}


def test_process_age_invalid():
    with pytest.raises(ValueError, match="Sayıya çevrilmedi."):
        process_age("abc")

def test_process_age_none():
    with pytest.raises(TypeError, match="Yaş None olamaz."):
        process_age(None)
def test_process_age_float():
    with pytest.raises(ValueError, match="Sayıya çevrilmedi."):
        process_age("25.5")
def test_process_age_negative():
    assert process_age(-5) == -10


def test_process_age_empty():
    with pytest.raises(ValueError, match="Sayıya çevrilmedi."):
        process_age("")