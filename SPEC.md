# QR Code Generator - Specification

## Purpose

The application will allow a user to enter text or a URL and generate a QR code that can be displayed and downloaded as a PNG image.

## Required Features

- Accept text or a URL from the user.
- Display a visible character counter.
- Reject empty input or input containing only whitespace.
- Display a warning when the input looks like a malformed URL without blocking QR generation.
- Generate and display a QR code on the page.
- Allow the user to download the QR code as a PNG file.
- Generate the download filename from the user's input using the existing safe_filename() function.
- Allow the user to control the QR code image size.
- Allow the user to select the foreground color.
- Allow the user to control the QR code border width.

## Application Structure

- The QR generation logic will be placed in a separate function.
- The QR generation function will accept arguments and return an image.
- The QR generation function will not contain Streamlit calls.
- The generated image will be stored in memory using io.BytesIO.
- No temporary image file will be required.
- The application will use the qrcode library and Pillow.
- All dependencies will be listed in requirements.txt.
- The existing safe_filename() function from Assignment 1 will be reused.

## Validation

- Empty input will display an error message instead of generating a QR code.
- Whitespace-only input will display an error message.
- A possible malformed URL will display a warning, but the user will still be allowed to generate the QR code.

## User Interface

The Streamlit interface will contain:

1. A text input area.
2. A character counter.
3. Image size control.
4. Foreground color control.
5. Border width control.
6. A Generate QR Code button.
7. A QR code preview.
8. A Download PNG button.

## Deliverables

The repository will contain:

- SPEC.md
- Application source code
- functions.py
- requirements.txt
- README.md
- A screenshot of the running application

The README will include instructions for installing dependencies and running the application from a clean clone.
