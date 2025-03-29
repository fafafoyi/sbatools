def is_even(n):
    return n % 2 == 0

def test_is_even():

    assert is_even(4) == True

def test_is_odd():

    assert is_even(3) == False

def test_is_zero_even():

    assert is_even(0) == True