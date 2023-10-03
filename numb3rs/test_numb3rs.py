import numb3rs

def test_validate():
    assert numb3rs.validate("1.2.3.4")
    assert numb3rs.validate("255.255.255.255")
    assert numb3rs.validate("0.0.0.0")
    assert not numb3rs.validate("1.2.3.999")
    assert not numb3rs.validate("2.3.4")
    assert not numb3rs.validate("4./1d34")