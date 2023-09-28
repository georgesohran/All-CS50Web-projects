from fuel import gauge, convert
import pytest


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(27) == "27%"
    assert gauge(51) == "51%"

def test_convert():
    with pytest.raises(ValueError):
        assert convert("13/10")
    with pytest.raises(ZeroDivisionError):
        assert convert("12/0")
    with pytest.raises(ValueError):
        assert convert("whaa")
#    assert convert("15/20") == 75
#    assert convert("99/100") == 99
