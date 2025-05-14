from src.findaverage import findaverage

def test_findaverage():
    assert findaverage(3, 3, 3) == 3.0
    assert findaverage(1, 2, 3) == 2.0
    assert findaverage(1, 2, 2) == 1.667

