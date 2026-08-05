import streamlit as st
import cv2
import numpy as np

st.title("**🖼️ Image Filters App**")

# File uploader
uploaded_file = st.file_uploader(
    "Upload an image", 
    type=["jpg", "jpeg", "png"], 
    key="uploader1"
)

if uploaded_file is not None:
    # Read image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    # Show original image
    st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="Original Image")

    # Buttons for filters
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    # col4, col5, col6 = st.columns(3)

    output_img = None
    action = None

    if col1.button("Gaussian Blur"):
        output_img = cv2.GaussianBlur(image, (5, 5), 3)
        action = "Gaussian Blur"

    if col2.button("Median Blur"):
        output_img = cv2.medianBlur(image, 5)
        action = "Median Blur"

    if col3.button("Bilateral Filter"):
        output_img = cv2.bilateralFilter(image, d=5, sigmaColor=75, sigmaSpace=75)
        action = "Bilateral Filter"

    if col4.button("Sharpening Image"):
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]], dtype=np.float32)
        output_img = cv2.filter2D(image, -1, kernel)
        action = "Sharpen"

    if col5.button("Canny Edge Detection"):
        output_img = cv2.Canny(image, 150, 160)
        action = "Canny Edge Detection"

    if col6.button("Threshold Image"):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, output_img = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        action = "Thresholding"

    # Show output image if any button clicked
    if output_img is not None:
        if len(output_img.shape) == 2:  # grayscale or edge maps
            st.image(output_img, caption=f"{action} Result", channels="GRAY")
        else:
            st.image(cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB), caption=f"{action} Result")
