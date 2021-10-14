from mersenne import generatePotentialMP, isPrime

def test_generatePotentialMP():
    assert(generatePotentialMP(2) == 3)
    assert(generatePotentialMP(1) ==1)

def test_isPrime():
    assert(isPrime(7))
    assert(isPrime(2))
    assert(isPrime(3))
    assert(isPrime(4) == False)