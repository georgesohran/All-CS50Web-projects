from fuel import gauge, convert

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(27) == "27%"
    assert gauge(51) == "51%"

def test_convert():
    assert convert(1) == "E"
    assert convert(100) == "F"
    assert convert(99) == "F"
    assert convert(27) == "27%"
    assert convert(51) == "51%"