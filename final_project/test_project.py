import project as p

def test_f():
    p.set_formula("x*2")
    assert p.f(12) == -24
    p.set_formula("x**2")
    assert p.f(-2) == -4
    p.set_formula("math.sqrt(x)")
    assert p.f(4) == -2

def test_restructure_formula():
    assert p.restructure_formula("x^3") == "x**3"
    assert p.restructure_formula("cos(x)") == "math.cos(x)"
    assert p.restructure_formula("x/4") == "x/4"

def test_def_range_of():
    assert p.def_range_of("x**3") == range(-100,100)
    assert p.def_range_of("math.sqrt(x)") == range(0,100)
