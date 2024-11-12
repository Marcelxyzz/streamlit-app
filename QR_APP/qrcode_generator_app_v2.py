import streamlit as st
from decode_qrcode_page import qrcode_decode
from generate_qrcode import qrcode_generate

st.image(image="https://www.the-qrcode-generator.com/wp-content/themes/tqrcg/img/custom-qr-code/hero-image.webp")

options = ["QR CODE GENERATOR", "QR CODE DECODER", "ABOUT ME"]

page_selection = st.sidebar.selectbox("Menu", options)

if page_selection == "QR CODE GENERATOR":
    qrcode_generate()
elif page_selection == "QR CODE DECODER":
    qrcode_decode()
elif page_selection == "ABOUT ME":
    st.title("ABOUT ME")
    st.image(image="https://media3.giphy.com/media/tHIRLHtNwxpjIFqPdV/giphy.webp?cid=790b76119v1x01707vgpuxkw0ds6hslfc4wgu610yrgdepfa&ep=v1_gifs_trending&rid=giphy.webp&ct=g")


