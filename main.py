import streamlit as st
import subprocess

def main():
    # Set page title and favicon
    st.set_page_config(page_title="Streamlit App", page_icon=":memo:")

    # Set custom CSS styles with background image
    st.markdown(
    """
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
    """,
    unsafe_allow_html=True
)
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


    st.title("What Function Would You Like to Perform?")

    # Create a container for the buttons
    button_container = st.empty()
    with button_container:
        col1, col2 = st.columns(2)

        # Button for Handwritten Text Recognition
        with col1:
            if st.button("Handwritten Text Recognition"):
                launch_app("HTR.py")

        # Button for Text Summarization
        with col2:
            if st.button("Text Summarization"):
                launch_app("summariser.py")

def launch_app(app_file):
    subprocess.Popen(["streamlit", "run", app_file])

if __name__ == "__main__":
    main()