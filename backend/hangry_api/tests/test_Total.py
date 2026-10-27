from types import SimpleNamespace

import pytest

from api.controllers import Total


@pytest.mark.parametrize(
    "quantities,prices,delivery_fee,expected",
    [
        ([2], [10.0], 3.50, 25.44),  # Mindestliefergebühr inklusive Steuer
        ([1, 2], [4.0, 3.0], 5.00, 16.24),  # Mehrere Artikelpositionen
        ([], [], 0.0, 0),  # Kein Betrag und keine Liefergebühr
        ([], [], 3.50, 3.79),  # Nur die Liefergebühr
    ],
)
def test_total(quantities, prices, delivery_fee, expected):
    # Einfache Objekte simulieren die Bestellpositionen.
    order = [
        SimpleNamespace(quantity=quantity, item=SimpleNamespace(price=price))
        for quantity, price in zip(quantities, prices)
    ]
    assert Total.calculate(order, delivery_fee) == expected
