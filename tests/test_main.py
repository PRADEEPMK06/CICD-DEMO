from app.main import check_factorial,check_prime

def test_check_factorial():
    assert check_factorial(5) == 120
    assert check_factorial(0) == 1
    assert check_factorial(1) == 1
    assert check_factorial(-4) == "Factorial is not defined for negative numbers"


def test_check_prime():
    assert check_prime(2) == True
    assert check_prime(3) == True
    assert check_prime(4) == False
    assert check_prime(5) == True
    assert check_prime(10) == False
    assert check_prime(13) == True