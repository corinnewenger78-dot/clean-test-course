import pytest
from types import SimpleNamespace
from api.controllers import Delivery


@pytest.mark.parametrize(
    "quantities,distance,expected",
    [
        ([], 0, 3.50),          # Leere Bestellung
        ([3, 1], 2, 3.50),     # Mindestgebühr
        ([5], 3, 3.50),        # Grenze: 5 Artikel
        ([6], 3, 3.50),        # Grenze: 3 Entfernungseinheiten
        ([6], 4, 5.00),        # Mittlere Liefergebühr
        ([10], 6, 5.00),       # Grenze: 10 Artikel
        ([11], 5, 5.00),       # Grenze: 5 Entfernungseinheiten
        ([11], 6, 7.50),       # Höchste Liefergebühr
        ([5, 5, 5], 6, 7.50),  # Mengen über mehrere Positionen
    ],
)
def test_delivery_fee(quantities, distance, expected):
    # Einfache Testobjekte ersetzen unnötige Datenbank-Mocks.
    order = [SimpleNamespace(quantity=quantity) for quantity in quantities]
    assert Delivery.calculate(order, distance) == expected
