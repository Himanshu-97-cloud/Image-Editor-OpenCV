# app.py
import streamlit as st
import cv2
import numpy as np
import main  # import your toolbox

st.title("🖼️ Image Editor (Photoshop Clone)")

uploaded_file = st.file_uploader(
    "Upload an image", 
    type=["jpg","jpeg","png"], 
    key="uploader1"
)

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="Original Image")

    st.sidebar.title("Edit Options")

    # Resize
    if st.sidebar.checkbox("Resize", key="resize"):
        w = st.sidebar.slider("Width", 50, 1000, image.shape[1], key="resize_w")
        h = st.sidebar.slider("Height", 50, 1000, image.shape[0], key="resize_h")
        resized = main.img_resize(image, w, h)
        st.image(cv2.cvtColor(resized, cv2.COLOR_BGR2RGB), caption="Resized Image")

    # Crop
    if st.sidebar.checkbox("Crop", key="crop"):
        startX = st.sidebar.slider("Start X", 0, image.shape[1], 0, key="crop_x1")
        endX = st.sidebar.slider("End X", 0, image.shape[1], image.shape[1], key="crop_x2")
        startY = st.sidebar.slider("Start Y", 0, image.shape[0], 0, key="crop_y1")
        endY = st.sidebar.slider("End Y", 0, image.shape[0], image.shape[0], key="crop_y2")
        cropped = main.img_crop(image, startY, endY, startX, endX)
        st.image(cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB), caption="Cropped Image")

    # Rotate
    if st.sidebar.checkbox("Rotate", key="rotate"):
        angle = st.sidebar.slider("Angle", -180, 180, 0, key="rotate_angle")
        rotated = main.img_rotate(image, angle)
        st.image(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB), caption="Rotated Image")

    # Flip
    if st.sidebar.checkbox("Flip", key="flip"):
        flip_mode = st.sidebar.selectbox("Flip Mode", ["Horizontal", "Vertical", "Both"], key="flip_mode")
        mode_map = {"Horizontal": 1, "Vertical": 0, "Both": -1}
        flipped = main.img_flip(image, mode_map[flip_mode])
        st.image(cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB), caption="Flipped Image")

    # Brightness & Contrast
    if st.sidebar.checkbox("Brightness/Contrast", key="bc"):
        alpha = st.sidebar.slider("Contrast", 0.5, 3.0, 1.0, key="contrast")
        beta = st.sidebar.slider("Brightness", -100, 100, 0, key="brightness")
        adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
        st.image(cv2.cvtColor(adjusted, cv2.COLOR_BGR2RGB), caption="Adjusted Image")

    # Grayscale
    if st.sidebar.checkbox("Grayscale", key="gray"):
        gray = main.img_grayscale(image)
        st.image(gray, caption="Grayscale", channels="GRAY")

    # HSV
    if st.sidebar.checkbox("HSV", key="hsv"):
        hsv = main.img_hsv(image)
        st.image(hsv, caption="HSV", channels="HSV")

    # Save
    if st.sidebar.button("Save Edited Image", key="save"):
        main.img_save(image, "edited_image.jpg")
        st.success("Image saved as edited_image.jpg")
