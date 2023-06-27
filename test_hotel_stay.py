import pytest
from tax_calc import HotelRoomStay, NightStay


def test_calculate_tax():
    stay = HotelRoomStay(200.00)
    # Tax rate is 5%, so tax should be 10.00
    assert stay.calculate_tax(5.0) == 10.00


def test_state_tax():
    stay = HotelRoomStay(200.00)
    # State tax rate is 4.45%, so tax should be 8.90
    assert stay.state_tax() == 8.90


def test_parish_tax():
    stay = HotelRoomStay(200.00)
    # Parish tax rate is 5.5%, so tax should be 11.00
    assert stay.parish_tax() == 11.00


def test_city_tax():
    stay = HotelRoomStay(200.00)
    # City tax rate is 3.0%, so tax should be 6.00
    assert stay.city_tax() == 6.00


def test_subtotal():
    stay = NightStay(200.00)
    # Room charge is 200.00, state tax is 8.90, parish tax is 11.00, city tax is 6.00
    # So, subtotal should be 225.90
    assert stay.subtotal() == 225.90


def test_zero_charge():
    stay = HotelRoomStay(0.00)
    assert stay.state_tax() == 0.00
    assert stay.parish_tax() == 0.00
    assert stay.city_tax() == 0.00
    assert stay.subtotal() == 0.00


def test_negative_charge():
    with pytest.raises(ValueError):
        stay = HotelRoomStay(-50.00)
        # Since the room charge cannot be negative, it should raise a ValueError
