import pytest
from source.producto import sumar, restar


def test_sumar():
    assert sumar(3, 5) == 8
    assert sumar(-1, 1) == 0

def test_restar():
    assert restar(10, 5) == 5
    assert restar(0, 5) == -5

if __name__ == "__main__":
    pytest.main()
