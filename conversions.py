def convertCelsiusToKelvin(celsius):
    """Converts Celsius to Kelvin."""
    return celsius + 273.15

def convertCelsiusToFahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def convertFahrenheitToCelsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def convertFahrenheitToKelvin(fahrenheit):
    """Converts Fahrenheit to Kelvin."""
    return (fahrenheit - 32) * 5/9 + 273.15

def convertKelvinToCelsius(kelvin):
    """Converts Kelvin to Celsius."""
    return kelvin - 273.15

def convertKelvinToFahrenheit(kelvin):
    """Converts Kelvin to Fahrenheit."""
    return (kelvin - 273.15) * 9/5 + 32
