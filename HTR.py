import streamlit as st
from PIL import Image
import pytesseract
import pyperclip
from io import BytesIO
from reportlab.pdfgen import canvas
from streamlit_cropper import st_cropper

# Function to perform HTR
def perform_htr(image):
    # Perform OCR using Tesseract
    recognized_text = pytesseract.image_to_string(image)
    return recognized_text

# Function to save text as PDF
def save_as_pdf(text):
    pdf_bytes = None
    try:
        # Create a BytesIO object to store the PDF
        buffer = BytesIO()

        # Create a canvas and save the text as PDF with proper formatting
        pdf_canvas = canvas.Canvas(buffer)
        pdf_canvas.setFont("Helvetica", 12)
        text_lines = text.split("\n")
        y = 800
        for line in text_lines:
            pdf_canvas.drawString(10, y, line)
            y -= 20
        pdf_canvas.save()

        # Set the buffer position to the beginning
        buffer.seek(0)

        # Get the PDF bytes
        pdf_bytes = buffer.getvalue()
    except Exception as e:
        st.error(f"Error occurred while saving as PDF: {str(e)}")
    return pdf_bytes

# Streamlit app
def main():
    st.title("Handwriting To Text (HTR)")
    st.write("Upload any image of a handwritten text to convert it")

    # Image upload
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Load and display the image
        image = Image.open(uploaded_file)
        
        # Image cropper
        cropped_image = st_cropper(image, realtime_update=True)

        # Perform HTR on the cropped image
        recognized_text = perform_htr(cropped_image)

        # Display the recognized text in a centered text box
        st.subheader("Recognized Text")
        text_box = st.text_area(label="", value=recognized_text, height=300, key="recognized_text")

        # Create a container for the buttons
        button_container = st.container()
        with button_container:
            col1, col2 = st.columns([3, 1])

            # Button for copying the text
            with col1:
                if st.button("Copy Text", key="copy_button"):
                    pyperclip.copy(recognized_text)
                    st.write("Copied To Clipboard")

            # Button for saving as PDF
            with col2:
                if st.button("Save as PDF", key="pdf_button"):
                    pdf_bytes = save_as_pdf(recognized_text)
                    if pdf_bytes is not None:
                        st.download_button("Download PDF", data=pdf_bytes, file_name='text.pdf')

# Custom CSS styles
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
CUSTOM_CSS = """
<style>
.stButton>button {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #4CAF50;
    color: white;
    padding: 1em 2em;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
}
.stButton>button:hover {
    background-color: #45a049;
}
.stButton>button:active {
    background-color: #3e8e41;
}
.stButton>button:focus {
    outline: none;
}
.stButton>button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}
.stButton>button:disabled:hover {
    background-color: #4CAF50;
}
</style>
"""

if __name__ == "__main__":
    # Add custom CSS styles
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    
    # Run the app
    main()
