import pytest
from source.producto import Producto


def test_inicializacion_producto():
    p = Producto(1, "producto 1", 50)
    assert p.id_producto == 1
    assert p.nombre == "producto 1"
    assert p.precio == 50


def test_str_producto():
    p = Producto(3, "producto 3", 20)
    assert str(p) == "Producto(id=3, nombre='producto 3', precio=20)"


@pytest.mark.parametrize(
    "precio, cantidad, esperado",
    [
        (50, 0, 0),
        (50, 2, 100),
        (20, 5, 100),
        (150, 3, 450),
    ],
)
def test_calcular_total(precio, cantidad, esperado):
    p = Producto(1, "item", precio)
    assert p.calcular_total(cantidad) == esperado


def test_calcular_total_cantidad_negativa_lanza_error():
    p = Producto(1, "producto 1", 50)
    with pytest.raises(ValueError, match="La cantidad no puede ser negativa."):
        p.calcular_total(-1)
