from api.controllers import Tax


def test_simple_tax():
    # Die Liefergebühr beträgt seit der Änderung mindestens 3.50.
    subtotal = 15
    delivery_fee = 3.50
    assert Tax.calculate(subtotal, delivery_fee) == 1.53


def test_zero_tax():
    # Ohne Kosten wird auch keine Steuer berechnet.
    assert Tax.calculate(0, 0) == 0
