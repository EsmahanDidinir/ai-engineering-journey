from data_processor import DataProcessor
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