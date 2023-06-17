room_charge: float = 192.00  # example: 141.00
state_tax_rate: float = 4.45  # always 4.45
parish_tax_rate: float = 5.5  # always 5.5
city_tax_rate: float = 3.0  # always 3.0


def state_tax(state_tax_rate: float, room_charge: float) -> float:
    """Calculates USD amount of State Tax charged to Louisiana hotel room.

    :param state_tax_rate: Known percentage of State Tax applied to room
    charge.
    :type state_tax_rate: float
    :param room_charge: Room rate for one night.
    :type room_charge: float
    :return: Returns `amount_taxed` rounded by 2.
    :rtype: float
    """
    tax_conversion = state_tax_rate / 100  # 4.45 -> 0.445
    amount_taxed = room_charge * tax_conversion
    return round(amount_taxed, 2)


def parish_tax(parish_tax_rate: float, room_charge: float) -> float:
    """Calculates USD amount of Parish Tax charged to Louisiana hotel room.

    :param parish_tax_rate: Known percentage of Parish Tax applied to room
    charge.
    :type parish_tax_rate: float
    :param room_charge: Room rate for one night.
    :type room_charge: float
    :return: Returns `amount_taxed` rounded by 2.
    :rtype: float
    """
    tax_conversion = parish_tax_rate / 100
    amount_taxed = room_charge * tax_conversion
    return round(amount_taxed, 2)


def city_tax(city_tax_rate: float, room_charge: float) -> float:
    """Calculates USD amount of City Tax charged to Louisiana hotel room.

    :param city_tax_rate: Known percentage of City Tax applied to room
    charge.
    :type city_tax_rate: float
    :param room_charge: Room rate for one night.
    :type room_charge: float
    :return: Returns `amount_taxed` rounded by 2.
    :rtype: float
    """
    tax_conversion = city_tax_rate / 100
    amount_taxed = room_charge * tax_conversion
    return round(amount_taxed, 2)


if __name__ == "__main__":
    print(f"\nRoom Charge: ${room_charge!s}")
    print(
        f"State Tax: %{state_tax_rate!s} (${state_tax(state_tax_rate, room_charge)!s})"
    )
    print(
        f"Parish Tax: %{parish_tax_rate!s} (${parish_tax(parish_tax_rate, room_charge)!s})"
    )
    print(f"City Tax: %{city_tax_rate!s} (${city_tax(city_tax_rate, room_charge)!s})")

    total_day_charge: float = (
        room_charge
        + state_tax(state_tax_rate, room_charge)
        + parish_tax(parish_tax_rate, room_charge)
        + city_tax(city_tax_rate, room_charge)
    )
    print(f"Total Day Charge: ${total_day_charge:.2f}\n")
