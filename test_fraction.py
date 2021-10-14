from fraction import Fraction

def test_equality():
    half = Fraction (1, 2)
    otherHalf = Fraction(1, 2)
    assert (half == otherHalf) #hiermee ga je de adressen van de objecten vergelijken, niet de waarde, hij zal dus een foutief resultaat geven

def test_multiply():
    half = Fraction(1,2)
    otherHalf = Fraction(1, 2)
    result = half.mult(otherHalf)
    assert(result == Fraction(1 , 4))

def test_differentObjectsAreNotEqual():
    half = Fraction(1, 2)
    assert(half != 1)

def test_fractionAsAString():
    half = Fraction(1,2)
    assert(str(half) == "1/2")

def test_reduction():           
    half = Fraction(1,2)
    otherHalf  = Fraction(2, 4)

def test_add():
    half = Fraction(1,2)
    otherHalf = Fraction(1,3)
    result = half.add(otherHalf)
    assert (result == Fraction (5,6 ))

def test_divideFractions():
    half = Fraction(1, 2)
    result = half.divide(half) 
    assert (result == Fraction(1, 2))
    assert (Fraction (3, 2) == Fraction (1,2).divide(Fraction(1, 3)))