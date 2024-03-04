class ConversionNotPossible(Exception):
    """Exception for invalid conversion attempts."""
    pass

def convert(from_unit, to_unit, value):
    """Converts a value from one unit to another.

    Args:
        from_unit (str): The unit you are converting from.
        to_unit (str): The unit you are converting to.
        value (float): The value in the from_unit.

    Returns:
        float: The converted value in the to_unit.

    Raises:
        ConversionNotPossible: If the conversion between the specified units is not supported.
    """
    # Handles direct and inverse conversions for temperature and distance
    conversion_formulas = {
        ('Celsius', 'Kelvin'): lambda c: c + 273.15,
        ('Celsius', 'Fahrenheit'): lambda c: (c * 9/5) + 32,
        ('Kelvin', 'Celsius'): lambda k: k - 273.15,
        ('Kelvin', 'Fahrenheit'): lambda k: (k - 273.15) * 9/5 + 32,
        ('Fahrenheit', 'Celsius'): lambda f: (f - 32) * 5/9,
        ('Fahrenheit', 'Kelvin'): lambda f: (f - 32) * 5/9 + 273.15,
        ('Miles', 'Yards'): lambda m: m * 1760,
        ('Miles', 'Meters'): lambda m: m * 1609.344,
        ('Yards', 'Miles'): lambda y: y / 1760,
        ('Yards', 'Meters'): lambda y: y * 0.9144,
        ('Meters', 'Miles'): lambda m: m / 1609.344,
        ('Meters', 'Yards'): lambda m: m / 0.9144,
    }

    # Check for conversion to the same unit
    if from_unit == to_unit:
        return value

    try:
        # Attempt to perform the conversion using the appropriate formula.
        conversion_function = conversion_formulas[(from_unit, to_unit)]
        return conversion_function(value)
    except KeyError:
        # If no conversion formula is found, raise an exception.
        raise ConversionNotPossible(f"Conversion from {from_unit} to {to_unit} is not possible.")

