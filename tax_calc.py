class HotelRoomStay:
    """Hotel room stay for a single night, with methods to calculate various taxes."""

    state_tax_rate: float = 4.45  # always 4.45
    parish_tax_rate: float = 5.5  # always 5.5
    city_tax_rate: float = 3.0  # always 3.0

    def __init__(self, room_charge: float):
        """Initializes with the given room charge."""
        self.room_charge = room_charge

    def calculate_tax(self, tax_rate: float) -> float:
        """Calculates tax based on the tax rate."""
        tax_conversion = tax_rate / 100
        amount_taxed = self.room_charge * tax_conversion
        return round(amount_taxed, 2)

    def state_tax(self) -> float:
        """Calculates state tax."""
        return self.calculate_tax(self.state_tax_rate)

    def parish_tax(self) -> float:
        """Calculates parish tax."""
        return self.calculate_tax(self.parish_tax_rate)

    def city_tax(self) -> float:
        """Calculates city tax."""
        return self.calculate_tax(self.city_tax_rate)

    def subtotal(self) -> float:
        """Calculates subtotal for the night."""
        return self.room_charge + self.state_tax() + self.parish_tax() + self.city_tax()


class NightStay(HotelRoomStay):
    """A single night's stay in a hotel, inheriting from HotelRoomStay."""

    def __init__(self, room_charge: float):
        """Initializes with the given room charge."""
        super().__init__(room_charge)


if __name__ == "__main__":
    while True:
        try:
            number_of_nights = int(input("How many nights in this stay? "))
            if number_of_nights < 1:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    stays: list = []
    for night in range(1, number_of_nights + 1):
        while True:
            try:
                room_rate: float = float(input(f"Enter the room rate for night {night}: "))
                if room_rate < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a positive number.")

        stays.append(NightStay(room_rate))

    total_charge: float = 0.0
    for i, stay in enumerate(stays, start=1):
        print(f"\nNight {i} details:")
        print(f"Room Charge: ${stay.room_charge}")
        print(f"State Tax: %{stay.state_tax_rate} (${stay.state_tax()})")
        print(f"Parish Tax: %{stay.parish_tax_rate} (${stay.parish_tax()})")
        print(f"City Tax: %{stay.city_tax_rate} (${stay.city_tax()})")
        print(f"Subtotal for Night {i}: ${stay.subtotal():.2f}\n")
        total_charge += stay.subtotal()
    print(f"Total Charge for the Stay: ${total_charge:.2f}")
