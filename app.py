import csv
import io
import zipfile
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
        back_color="white",
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


def unique_filename(name, used_names):
    """Return a safe unique PNG filename."""
    base = safe_filename(name.strip())

    if not base:
        base = "qr_code"

    base = base[:40]

    candidate = base
    counter = 2

    while candidate.lower() in used_names:
        candidate = f"{base}_{counter}"
        counter += 1

    used_names.add(candidate.lower())

    return f"{candidate}.png"


def read_batch_csv(uploaded_file):
    """Read CSV and return valid and rejected rows."""
    valid_rows = []
    rejected_rows = []

    try:
        content = uploaded_file.getvalue().decode("utf-8-sig")
    except UnicodeDecodeError:
        return [], [
            {
                "row": "-",
                "reason": "The CSV file must use UTF-8 encoding.",
            }
        ]

    try:
        reader = csv.DictReader(io.StringIO(content))

        if reader.fieldnames is None:
            return [], [
                {
                    "row": "-",
                    "reason": "The CSV file is empty or has no header.",
                }
            ]

        normalized_headers = {
            header.strip().lower(): header
            for header in reader.fieldnames
            if header is not None
        }

        if "name" not in normalized_headers or "url" not in normalized_headers:
            return [], [
                {
                    "row": "-",
                    "reason": "Missing required columns: name and url.",
                }
            ]

        name_column = normalized_headers["name"]
        url_column = normalized_headers["url"]

        for row_number, row in enumerate(reader, start=2):
            name = (row.get(name_column) or "").strip()
            url = (row.get(url_column) or "").strip()

            if not name and not url:
                rejected_rows.append(
                    {
                        "row": row_number,
                        "reason": "Row contains only whitespace or is blank.",
                    }
                )
                continue

            if not name:
                rejected_rows.append(
                    {
                        "row": row_number,
                        "reason": "Name is blank.",
                    }
                )
                continue

            if not url:
                rejected_rows.append(
                    {
                        "row": row_number,
                        "reason": "URL is blank.",
                    }
                )
                continue

            if looks_like_malformed_url(url):
                rejected_rows.append(
                    {
                        "row": row_number,
                        "reason": "URL appears malformed.",
                    }
                )
                continue

            valid_rows.append(
                {
                    "name": name,
                    "url": url,
                }
            )

    except csv.Error as error:
        return [], [
            {
                "row": "-",
                "reason": f"Could not read CSV: {error}",
            }
        ]

    return valid_rows, rejected_rows


def build_batch_zip(
    valid_rows,
    box_size,
    border,
    foreground_color,
):
    """Generate all valid QR codes and return a ZIP in memory."""
    zip_buffer = io.BytesIO()
    used_names = set()

    with zipfile.ZipFile(
        zip_buffer,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
    ) as zip_file:

        for row in valid_rows:
            qr_image = generate_qr(
                data=row["url"],
                box_size=box_size,
                border=border,
                foreground_color=foreground_color,
            )

            image_buffer = io.BytesIO()
            qr_image.save(image_buffer, format="PNG")

            filename = unique_filename(
                row["name"],
                used_names,
            )

            zip_file.writestr(
                filename,
                image_buffer.getvalue(),
            )

    zip_buffer.seek(0)
    return zip_buffer.getvalue()


st.set_page_config(
    page_title="QR Code Generator",
    page_icon="📱",
)

st.title("QR Code Generator")

mode = st.radio(
    "Choose mode",
    ["Single code", "Batch from CSV"],
    horizontal=True,
)

box_size = st.slider(
    "Image size",
    min_value=5,
    max_value=20,
    value=10,
    help="QR module size range: 5–20 pixels.",
)

foreground_color = st.color_picker(
    "Foreground color",
    "#000000",
)

border = st.slider(
    "Border width",
    min_value=1,
    max_value=10,
    value=4,
    help="Border width range: 1–10 modules.",
)


if mode == "Single code":
    st.subheader("Single QR Code")

    st.write(
        "Enter text or a URL to create a downloadable QR code."
    )

    user_input = st.text_area(
        "Text or URL",
        placeholder="Enter text or a URL here...",
    )

    st.caption(f"Characters: {len(user_input)}")

    if user_input.strip() and looks_like_malformed_url(user_input):
        st.warning(
            "This input looks like a URL but may be malformed. "
            "You can still generate the QR code."
        )

    if st.button("Generate QR Code"):
        if not user_input.strip():
            st.error(
                "Please enter text or a URL before generating a QR code."
            )

        else:
            qr_image = generate_qr(
                data=user_input.strip(),
                box_size=box_size,
                border=border,
                foreground_color=foreground_color,
            )

            st.image(
                qr_image,
                caption="Generated QR Code",
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


else:
    st.subheader("Batch QR Codes from CSV")

    st.write(
        "Upload a CSV file containing the columns `name` and `url`."
    )

    uploaded_file = st.file_uploader(
        "Upload CSV",
        type=["csv"],
    )

    if uploaded_file is not None:
        valid_rows, rejected_rows = read_batch_csv(uploaded_file)

        st.subheader("Batch Preview")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Valid rows",
                len(valid_rows),
            )

        with col2:
            st.metric(
                "Rejected rows",
                len(rejected_rows),
            )

        if valid_rows:
            st.write("Valid rows")
            st.dataframe(
                valid_rows,
                use_container_width=True,
            )

        if rejected_rows:
            st.write("Rejected rows")
            st.dataframe(
                rejected_rows,
                use_container_width=True,
            )

            for rejected in rejected_rows:
                st.warning(
                    f"Row {rejected['row']}: "
                    f"{rejected['reason']}"
                )

        if valid_rows:
            zip_data = build_batch_zip(
                valid_rows=valid_rows,
                box_size=box_size,
                border=border,
                foreground_color=foreground_color,
            )

            st.success(
                f"Ready to generate {len(valid_rows)} QR code(s)."
            )

            st.download_button(
                label="Download QR Codes ZIP",
                data=zip_data,
                file_name="qr_codes.zip",
                mime="application/zip",
            )

        else:
            st.info(
                "There are no valid rows available to generate QR codes."
            )
