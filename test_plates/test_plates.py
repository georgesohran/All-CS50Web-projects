from plates import is_valid

def test_is_valid_cercount():
    assert is_valid("AAA232")
    assert is_valid("ABCD")
    assert not is_valid("ABCDEFG1")

def test_is_valid_symbols():
    assert not is_valid("ADA,!E")
    assert not is_valid("!ALAW")

def test_is_valid_last_cer():
    assert is_valid("SAS21")
    assert not is_valid("LIR23E")

def test_is_valid_first_num():
    assert is_valid("LRIP1")
    assert not is_valid("LIR001")

def test_is_valid_first_cer():
    assert is_valid("CS50")
    assert not is_valid("A123")


