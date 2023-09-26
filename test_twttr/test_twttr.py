from twttr import shorten

def test_shorten_lower():
    assert shorten("word") == "wrd"
    assert shorten("twitter") == "twttr"
    assert shorten("low") == "lw"

def test_shorten_upper():
    assert shorten("WORD") == "WRD"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("UPPER") == "PPR"

def test_shorten_letters():
    assert shorten("AEIOU n") == " n"
