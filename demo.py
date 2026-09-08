from functions import (
    celsius_to_fahrenheit,
    line_total,
    initials,
    is_valid_str,
    truncate,
    safe_filename,
)

# Valid tests
print(celsius_to_fahrenheit(25))
print(line_total(10, 3))
print(initials("Luis De Leon"))
print(is_valid_str("Hello"))
print(truncate("Hello World", 5))
print(safe_filename('My File/Test "One"'))

# Rejected input tests
tests = [
    lambda: celsius_to_fahrenheit("hot"),
    lambda: line_total(10, -2),
    lambda: initials(123),
    lambda: is_valid_str(123),
    lambda: truncate("Hello", -1),
    lambda: safe_filename(123),
]

for test in tests:
    try:
        print(test())
    except (TypeError, ValueError) as error:
        print("Rejected:", error)