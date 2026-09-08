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


def initials(full_name):
    """Turn a full name into uppercase initials."""
    if not isinstance(full_name, str):
        raise TypeError("Name must be text.")

    words = full_name.strip().split()

    if not words:
        return ""

    return "".join(word[0].upper() for word in words)


def is_valid_str(text):
    """Return True if the text contains non-space characters."""
    if not isinstance(text, str):
        raise TypeError("Input must be text.")

    return text.strip() != ""
def truncate(text, limit=20):
    """Shorten text to a limit and add an ellipsis if shortened."""
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")
    if limit < 0:
        raise ValueError("Limit cannot be negative.")

    if len(text) > limit:
        return text[:limit] + "..."

    return text


def safe_filename(text):
    """Turn text into a safe filename."""
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")

    return text.replace(" ", "_").replace("/", "_").replace('"', "").replace("'", "")