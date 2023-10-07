from seasons import convert_date

def test_convert_date():
    assert convert_date("1999-01-01") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert_date("")