from fuel import gauge, convert
import pytest


def test_gauge():
    assert gauge(124) == None
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(27) == "27%"
    assert gauge(51) == "51%"

def test_convert():
    assert convert("13/10") == 130
    assert convert("12/0") == None
    assert convert("whaa") == None
    assert convert("15/20") == 75
    assert convert("99/100") == 99
