import streamlit as st
from utils import generate_qr

st.set_page_config(
    page_title="QR Code Generator",
    page_icon="🔳",
    layout="centered"
)

st.title("QR Code Generator")
st.write("Generate QR codes locally. Free. No expiry.")

with st.form("qr_form"):
    data = st.text_input(
        "Data",
        placeholder="URL, text, email, WiFi config, anything"
    )

    col1, col2 = st.columns(2)

    with col1:
        fill_color = st.color_picker("QR color", "#000000")

    with col2:
        back_color = st.color_picker("Background color", "#ffffff")

    box_size = st.slider("QR size", 5, 20, 10)
    border = st.slider("Border", 1, 10, 4)

    submitted = st.form_submit_button("Generate QR")

if submitted:
    if not data.strip():
        st.error("Please enter some data.")
    else:
        qr_image = generate_qr(
            data=data,
            fill_color=fill_color,
            back_color=back_color,
            box_size=box_size,
            border=border,
        )

        st.success("QR code generated.")
        st.image(qr_image, width=300)

        st.download_button(
            label="Download PNG",
            data=qr_image,
            file_name="qr_code.png",
            mime="image/png"
        )

st.markdown("---")
st.markdown(
    "<p style='text-align:center; font-size:12px; color:gray;'>"
    "Developed by Muhammad Usman Khan"
    "</p>",
    unsafe_allow_html=True
)