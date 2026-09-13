import io
from urllib.parse import urlparse

import qrcode
import streamlit as st

from functions import safe_filename


def generate_qr(data, box_size, border, foreground_color):
    """Generate and return a QR code image."""
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )

    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(
        fill_color=foreground_color,
        back_color="white"
    )

    return image.convert("RGB")


def looks_like_malformed_url(text):
    """Return True when input looks like a URL but appears malformed."""
    value = text.strip()

    if not value:
        return False

    lower_value = value.lower()

    looks_like_url = (
        lower_value.startswith("http")
        or lower_value.startswith("www.")
        or ("." in value and " " not in value)
    )

    if not looks_like_url:
        return False

    if not lower_value.startswith(("http://", "https://")):
        value = "https://" + value

    parsed = urlparse(value)

    return not bool(parsed.netloc and "." in parsed.netloc)


st.set_page_config(
    page_title="QR Code Generator",
    page_icon="📱"
)

st.title("QR Code Generator")
st.write("Enter text or a URL to create a downloadable QR code.")

user_input = st.text_area(
    "Text or URL",
    placeholder="Enter text or a URL here..."
)

st.caption(f"Characters: {len(user_input)}")

box_size = st.slider(
    "Image size",
    min_value=5,
    max_value=20,
    value=10,
    help="QR module size range: 5–20 pixels."
)

foreground_color = st.color_picker(
    "Foreground color",
    "#000000"
)

border = st.slider(
    "Border width",
    min_value=1,
    max_value=10,
    value=4,
    help="Border width range: 1–10 modules."
)

if user_input.strip() and looks_like_malformed_url(user_input):
    st.warning(
        "This input looks like a URL but may be malformed. "
        "You can still generate the QR code."
    )

if st.button("Generate QR Code"):
    if not user_input.strip():
        st.error("Please enter text or a URL before generating a QR code.")

    else:
        qr_image = generate_qr(
            data=user_input.strip(),
            box_size=box_size,
            border=border,
            foreground_color=foreground_color,
        )

        st.image(
            qr_image,
            caption="Generated QR Code"
        )

        image_buffer = io.BytesIO()
        qr_image.save(image_buffer, format="PNG")
        image_buffer.seek(0)

        filename_base = safe_filename(user_input.strip())

        if not filename_base:
            filename_base = "qr_code"

        filename_base = filename_base[:40]

        st.download_button(
            label="Download PNG",
            data=image_buffer.getvalue(),
            file_name=f"{filename_base}.png",
            mime="image/png",
        )
