def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    if not isinstance(c, (int, float)):
        raise TypeError("Temperature must be a number.")
    return (c * 9 / 5) + 32


def line_total(price, qty):
    """Return the total price for a quantity of items."""
    if not isinstance(price, (int, float)):
        raise TypeError("Price must be a number.")
    if not isinstance(qty, (int, float)):
        raise TypeError("Quantity must be a number.")
    if qty < 0:
        raise ValueError("Quantity cannot be negative.")
    return price * qty