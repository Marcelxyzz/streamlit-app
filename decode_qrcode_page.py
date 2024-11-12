import streamlit as st
import numpy as np
import cv2


def qrcode_decode():
    st.header("QR CODE DECODER")

    qrcode = st.file_uploader("Upload you QR Code", type=["jpeg", "png", "jpg"])

    if qrcode:
        file_bytes = np.asarray(bytearray(qrcode.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

        st.image(opencv_image)

        detector = cv2.QRCodeDetector()
        decoded_info, point, straight_qr = detector.detectAndDecode(opencv_image)
        st.write(f"Your QR Code contains the following url: {decoded_info}")
