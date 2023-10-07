from seasons import convert_date

def test_convert_date():
    assert convert_date("January 1, 1999",) == "Invalid date"
    assert convert_date("1999-01-01") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert_date("1999-12-31") == "One thousand, four hundred forty minutes"
    assert convert_date("1970-01-01") == "Fifteen million, seven hundred seventy-eight thousand eighty minutes"
