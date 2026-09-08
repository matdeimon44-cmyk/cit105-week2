from functions import (
    celsius_to_fahrenheit,
    line_total,
    initials,
    is_valid_str,
    truncate,
    safe_filename,
)

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))

print(line_total(10, 3))
print(line_total(5.5, 2))

print(initials("Luis De Leon"))
print(initials("  Matthew Fernando Espinel Ricardo  "))

print(is_valid_str("Hello"))
print(is_valid_str("     "))

print(truncate("Hello World", 5))
print(truncate("Short", 10))

print(safe_filename('My File/Test "One"'))
print(safe_filename("week 2 assignment"))