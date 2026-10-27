from types import SimpleNamespace
from api.controllers import Subtotal


def test_simple_cost():
    # Drei Positionen mit jeweils fünf Artikeln zu 1.00.
    order = [
        SimpleNamespace(quantity=5, item=SimpleNamespace(price=1.0))
        for _ in range(3)
    ]
    assert Subtotal.calculate(order) == 15


def test_complex_cost():
    # Unterschiedliche Mengen und Preise werden aufsummiert.
    order = [
        SimpleNamespace(quantity=2, item=SimpleNamespace(price=3.5)),
        SimpleNamespace(quantity=1, item=SimpleNamespace(price=4.5)),
    ]
    assert Subtotal.calculate(order) == 11.5


def test_empty_order():
    # Eine leere Bestellung hat keinen Warenwert.
    assert Subtotal.calculate([]) == 0
