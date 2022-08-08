from Pressure.pressure import calculation

def test_calculation():
    assert calculation(9100, 1300, 35) == (25.87, 20.38)