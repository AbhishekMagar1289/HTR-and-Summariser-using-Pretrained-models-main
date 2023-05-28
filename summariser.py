import streamlit as st
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from heapq import nlargest
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import pyperclip
from io import BytesIO
import base64

# Download required NLTK resources
import nltk
nltk.download('punkt')
nltk.download('stopwords')

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

# Function to summarize the text
def summarize_text(text):
    if len(text.split()) < 50:
        return "Error: The text must be more than 50 words."
    else:
        sentences = sent_tokenize(text)
        stop_words = set(stopwords.words('english'))
        word_freq = {}
        for sentence in sentences:
            for word in sentence.split(' '):
                if word.lower() not in stop_words:
                    if word not in word_freq:
                        word_freq[word] = 1
                    else:
                        word_freq[word] += 1
        
        sentence_scores = {}
        for sentence in sentences:
            for word in sentence.split(' '):
                if word.lower() in word_freq:
                    if len(sentence.split(' ')) < 30:
                        if sentence not in sentence_scores:
                            sentence_scores[sentence] = word_freq[word]
                        else:
                            sentence_scores[sentence] += word_freq[word]
        
        summarized_sentences = nlargest(3, sentence_scores, key=sentence_scores.get)
        summarized_text = ' '.join(summarized_sentences)
        return summarized_text

# Create a Streamlit web app
def main():
    st.title("Text Summarizer")
    
    # Initialize session state
    if 'summarized_text' not in st.session_state:
        st.session_state.summarized_text = None
    
    # Text input
    text_input = st.text_area("Enter your text:", height=200)
    
    # Summarize button
    if st.button("Summarize"):
        summarized_text = summarize_text(text_input)
        st.session_state.summarized_text = summarized_text
        
        # Display summarized text
        st.subheader("Summarized Text")
        st.markdown(f"> {summarized_text}")
    
    # Copy text button
    if st.button("Copy Text"):
        if st.session_state.summarized_text:
            formatted_text = f"Summarized Text:\n{st.session_state.summarized_text}"
            pyperclip.copy(formatted_text)
            st.write("Text copied to clipboard.")
        else:
            st.write("Please summarize the text first.")
    
    # Save as PDF button
    if st.button("Save as PDF"):
        if st.session_state.summarized_text:
            try:
                pdf_data = save_pdf(st.session_state.summarized_text)
                download_link(pdf_data, "summary.pdf", "Download PDF")
                st.write("PDF saved successfully.")
            except Exception as e:
                st.write(f"Error occurred while saving PDF: {str(e)}")
        else:
            st.write("Please summarize the text first.")

# Function to save the summarized text as a PDF
def save_pdf(text):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    content = [Paragraph(text, styles["BodyText"])]
    doc.build(content)
    buffer.seek(0)
    return buffer

# Function to generate a download link for the PDF
def download_link(buffer, filename, text):
    b64 = base64.b64encode(buffer.read()).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="{filename}">{text}</a>'
    st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
