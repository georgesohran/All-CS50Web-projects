from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        assert Jar(-5)
    with pytest.raises(ValueError):
        assert Jar(0)
    with pytest.raises(ValueError):
        assert not Jar(5)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(5)
    assert jar.size == 6


def test_withdraw():
    jar = Jar()
    jar._size = 10
    jar.withdraw(1)
    assert jar.size == 9
    jar.withdraw(3)
    assert jar.size == 6
    jar.withdraw(6)
    assert jar.size == 0
    with pytest.raises(ValueError):
        assert not jar.withdraw(6)
