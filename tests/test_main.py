import pytest
from source.producto import Producto


def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5

if __name__ == "__main__":
    pytest.main()
