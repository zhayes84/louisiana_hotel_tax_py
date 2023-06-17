# Louisiana Hotel Tax Calculator

This Python script calculates the total daily charge for a hotel room in Louisiana, USA, by adding the room charge to the state, parish, and city taxes.

## Code Overview

The script contains three functions, each calculating a different tax:

1. `state_tax(state_tax_rate: float, room_charge: float) -> float`: This function calculates the amount of State Tax charged to the hotel room. The State Tax rate is always 4.45%.

2. `parish_tax(parish_tax_rate: float, room_charge: float) -> float`: This function calculates the amount of Parish Tax charged to the hotel room. The Parish Tax rate is always 5.5%.

3. `city_tax(city_tax_rate: float, room_charge: float) -> float`: This function calculates the amount of City Tax charged to the hotel room. The City Tax rate is always 3.0%.

The script also contains a main section that prints out the room charge, each of the taxes, and the total daily charge.

## Usage

You can run the script directly from the command line:

```bash
python3 tax_calculator.py
```

The output will look something like this:

```
Room Charge: $192.00
State Tax: %4.45 ($8.54)
Parish Tax: %5.5 ($10.56)
City Tax: %3.0 ($5.76)
Total Day Charge: $216.86
```

## Customization

You can customize the room charge by modifying the `room_charge` variable at the top of the script. The tax rates are constants and should not be changed unless the tax rates in Louisiana change.

## Dependencies

This script requires Python 3.6 or later. No external libraries are needed.

## License

This project is licensed under the terms of the MIT license.
