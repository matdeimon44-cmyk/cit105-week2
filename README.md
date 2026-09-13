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

---

# Assignment 2 - QR Code Generator

## Description

This application is a QR Code Generator built with Python and Streamlit. It allows a user to enter text or a URL, generate a scannable QR code, display it on the screen, and download it as a PNG image.

## Features

- Accepts text or a URL.
- Displays a character counter.
- Generates and displays a scannable QR code.
- Allows the QR code to be downloaded as a PNG.
- Creates the download filename from the user's input using `safe_filename()`.
- Allows control of the image size.
- Allows selection of the foreground color.
- Allows control of the border width.
- Rejects empty and whitespace-only input.
- Displays a warning when the input looks like a malformed URL.
- Generates the QR image in memory using `io.BytesIO`.

## Screenshot

![QR Code Generator](qr_app_screenshot.png)

## Requirements

- Python 3
- Streamlit
- qrcode
- Pillow

## Installation from a Clean Clone

Clone the repository:

```bash
git clone https://github.com/matdeimon44-cmyk/cit105-week2.git
```

Enter the repository:

```bash
cd cit105-week2
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed by Streamlit in your web browser.

## How to Use

1. Enter text or a URL.
2. Select the image size.
3. Choose a foreground color.
4. Select the border width.
5. Click **Generate QR Code**.
6. Scan the generated QR code with a phone camera.
7. Click **Download PNG** to save the QR code.

## Testing

The application was tested by generating a QR code containing a URL and scanning it with a phone camera. The generated QR code successfully opened the expected URL.

## Live Application

The QR Code Generator is deployed on Streamlit Community Cloud.

https://cit105-week2-9umhbtrc78phztywwnzany.streamlit.app/
