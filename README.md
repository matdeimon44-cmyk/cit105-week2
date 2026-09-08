# CIT 105 Week 2 - Function Library Exercise Set

This project contains six reusable Python functions and a demo file that tests each function.

## Functions

### celsius_to_fahrenheit(c)
Converts a Celsius temperature to Fahrenheit.

- Input: a number representing Celsius
- Returns: the Fahrenheit temperature
- Rejects: non-numeric input with a TypeError

### line_total(price, qty)
Calculates the total price by multiplying price by quantity.

- Input: numeric price and quantity
- Returns: total price
- Rejects: non-numeric input and negative quantities

### initials(full_name)
Creates uppercase initials from a full name.

- Input: a string containing a name
- Returns: uppercase initials
- Rejects: non-string input
- Handles extra spaces and empty strings

### is_valid_url(text)
Checks whether a string contains non-space characters.

- Input: a string
- Returns: True or False
- Rejects: non-string input
- Returns False for empty strings or strings containing only spaces

### truncate(text, limit=20)
Shortens text when it is longer than the specified limit.

- Input: text and an optional character limit
- Returns: the original text or shortened text with "..."
- Rejects: invalid input types and negative limits

### safe_filename(text)
Converts text into a safer filename.

- Input: a string
- Returns: a filename without spaces, slashes, or quotes
- Rejects: non-string input

## Demo

The `demo.py` file imports all six functions and calls each function at least twice with different inputs.