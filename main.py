import streamlit as st
from PIL import Image
import rembg
import base64
import os

def remove_background(image):
    return rembg.remove(image)

def main():
    st.title("Background Removal App")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        if st.button("Remove Background"):
            st.write("Removing background...")

            # Process image and remove background
            with st.spinner("Processing..."):
                image = Image.open(uploaded_file).convert("RGBA")
                image_with_transparent_bg = remove_background(image)

            st.success("Background removed successfully!")

            # Display the image with a transparent background
            st.image(image_with_transparent_bg, caption="Image with Transparent Background", use_column_width=True)

            # Save the image to a temporary file for download
            temp_file_path = "output_image.png"
            image_with_transparent_bg.save(temp_file_path, format="PNG")

            # Offer download link for the processed image
            with st.spinner("Creating Download link"):
                st.markdown(get_binary_file_downloader_html(temp_file_path, 'Image with Transparent Background'), unsafe_allow_html=True)

def get_binary_file_downloader_html(file_path, file_label='File'):
    with open(file_path, 'rb') as file:
        data = file.read()
    b64 = base64.b64encode(data).decode()
    return f'<a href="data:file/png;base64,{b64}" download="{file_label}.png">Download {file_label}</a>'

if __name__ == "__main__":
    main()
