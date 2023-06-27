# Hotel Stay Tax Calculator

This program calculates the tax for each night stay in a hotel based on room rates, state tax, parish tax, and city tax. The users are asked to enter the number of nights for the stay, and the room rate for each night. The program then calculates the tax for each type (state, parish, and city) and gives a summary for each night and a total for the entire stay.

## Code

The code consists of two classes: `HotelRoomStay` and `NightStay`. The `HotelRoomStay` class is responsible for calculating the different types of taxes and the subtotal for each night. The `NightStay` class, which inherits from `HotelRoomStay`, is used to create instances for each night's stay.

A brief summary of the methods in `HotelRoomStay`:

- `calculate_tax(self, tax_rate: float) -> float:`: Generic method to calculate tax.
- `state_tax(self) -> float:`: Calculates state tax.
- `parish_tax(self) -> float:`: Calculates parish tax.
- `city_tax(self) -> float:`: Calculates city tax.
- `subtotal(self) -> float:`: Calculates subtotal for the night.

In the main part of the code, the user is prompted to enter the number of nights for the stay and the room rate for each night. The program then calculates the tax and subtotal for each night, and finally the total charge for the entire stay.

## Tests

The `pytest` framework is used to test the classes and methods. Each test function tests a specific method in the `HotelRoomStay` class or a specific scenario (such as zero or negative room charge).

## Usage

To run the program, execute the main Python file in your terminal. To run the tests, execute the test Python file in your terminal using `pytest`.

## Future improvements

The current program assumes a specific tax rate for state, parish, and city. A possible improvement would be to allow these rates to be changed, or to allow different rates for different hotels or locations. Also, the user input validation could be improved to handle more edge cases and invalid inputs.
