from bank import value

def test_value():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hey") == 20
    assert value("Hey") == 20
    assert value("hmmmm") == 100
    assert value("AAAA") == 100