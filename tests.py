import unittest
from conversions import (convertCelsiusToKelvin, convertCelsiusToFahrenheit,
                         convertFahrenheitToCelsius, convertFahrenheitToKelvin,
                         convertKelvinToCelsius, convertKelvinToFahrenheit)

class TestTemperatureConversions(unittest.TestCase):
    def test_convertCelsiusToKelvin(self):
        test_cases = [
            (-273.15, 0),  # Absolute zero
            (0, 273.15),  # Freezing point of water
            (100, 373.15),  # Boiling point of water
        ]
        for input_temp, expected in test_cases:
            self.assertAlmostEqual(convertCelsiusToKelvin(input_temp), expected, places=2)

    def test_convertCelsiusToFahrenheit(self):
        test_cases = [
            (-273.15, -459.67),  # Absolute zero
            (0, 32),  # Freezing point of water
            (100, 212),  # Boiling point of water
        ]
        for input_temp, expected in test_cases:
            self.assertAlmostEqual(convertCelsiusToFahrenheit(input_temp), expected, places=2)

    def test_convertFahrenheitToCelsius(self):
        test_cases = [
            (-459.67, -273.15),  # Absolute zero
            (32, 0),  # Freezing point of water
            (212, 100),  # Boiling point of water
        ]
        for input_temp, expected in test_cases:
            self.assertAlmostEqual(convertFahrenheitToCelsius(input_temp), expected, places=2)

    def test_convertFahrenheitToKelvin(self):
        test_cases = [
            (-459.67, 0),  # Absolute zero
            (32, 273.15),  # Freezing point of water
            (212, 373.15),  # Boiling point of water
        ]
        for input_temp, expected in test_cases:
            self.assertAlmostEqual(convertFahrenheitToKelvin(input_temp), expected, places=2)

    def test_convertKelvinToCelsius(self):
        test_cases = [
            (0, -273.15),  # Absolute zero
            (273.15, 0),  # Freezing point of water
            (373.15, 100),  # Boiling point of water
        ]
        for input_temp, expected in test_cases:
            self.assertAlmostEqual(convertKelvinToCelsius(input_temp), expected, places=2)

    def test_convertKelvinToFahrenheit(self):
        test_cases = [
            (0, -459.67),  # Absolute zero
            (273.15, 32),  # Freezing point of water
            (373.15, 212),  # Boiling point of water
        ]
        for input_temp, expected in test_cases:
            self.assertAlmostEqual(convertKelvinToFahrenheit(input_temp), expected, places=2)

if __name__ == '__main__':
    unittest.main()
