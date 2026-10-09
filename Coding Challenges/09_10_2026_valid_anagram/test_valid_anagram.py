from valid_anagram import is_anagram

def test_valid_anagram():
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("a!", "!a") is True

def test_invalid_anagram():
    assert is_anagram("rat", "car") is False
    assert is_anagram("aacc", "ccac") is False

def test_empty_anagram():
    assert is_anagram("", "") is True

def test_different_anagram_counts():
    assert is_anagram("12354", "1234") is False

def test_different_case_anagram():
    assert is_anagram("AbcD", "aBCd") is False