HTR-and-Summariser-using-Pretrained-models
For running either models just use the code 'streamlit run main.py' .

Functional Dependanciies-

Python
streamlit library
stream_crop
tesseract ocr engine along with pytesseract library
Handwritten text refers to any form of written content that has been produced by hand using a pen, pencil, or other writing instruments, as opposed to being typed or printed. Handwritten text can vary in style, legibility, and quality, depending on the individual's handwriting skills and the circumstances under which it was written. It is a form of communication that has been used for centuries and is still prevalent today, despite the increasing use of digital technologies.

Over the course of this project i tried many scratch implementation models which used CNN and RNN combination architecture and the training was done using the IAM dataset the link for downloading it is - https://fki.tic.heia-fr.ch/databases/iam-handwriting-database

Performance analysis-

I havent provided the metrics for evaluation of scratch models but one thing was clear. If the code was implemented using scratch model, it would have become increasingly complex since for multiple lines of HTR, the amount of preprocessing required is very high and post processing is also required.
The pre trained models recognize sentences more effectively as compared to scratch models in many cases
However this doesnt mean that pre trained models provide perfect results. Even pre trained models are far from accurate when it comes to images that have slightly bad handwriting. The model misclassified letters many times if the letter was written in a slightly fancy way.
Training the tesseract engine on more data might be the way to go but not highly effective.
