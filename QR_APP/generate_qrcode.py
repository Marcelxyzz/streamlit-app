import streamlit as st
import segno
import time
def qrcode_generate():
    st.header("QR CODE GENERATOR")
    url = st.text_input("Insert URL")

    def generate_qr(url):
        qrcode = segno.make_qr(url)
        # qrcode.save("images/qrcode_streamlit.png", scale=10)
        qrcode.to_pil(scale=10,
                      dark="red", light="lightblue").save("images/qrcode_streamlit.png")


# only show qrcode if if somebody entered a url
    if url:
        with st.spinner("Generating QR code..."):
            time.sleep(3)
        generate_qr(url)
        st.image(image="images/qrcode_streamlit.png")

    st.markdown("Made by Marcel Metzger.")
