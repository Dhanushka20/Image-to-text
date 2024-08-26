# Document Digitalization App

This is a Python-based desktop application for converting images of documents into text using Optical Character Recognition (OCR). The application is built using the Tkinter GUI toolkit and leverages the Tesseract OCR engine for extracting text from images. The extracted text can be saved into a CSV file.

## Features

- **Image Upload:** Upload images in various formats such as PNG, JPG, JPEG, BMP, and GIF.
- **Text Extraction:** Extract text from the uploaded image using Tesseract OCR.
- **Text Display:** View the extracted text in the application interface.
- **Save to CSV:** Save the extracted text to a CSV file for further processing or analysis.

## Prerequisites

Before running the application, ensure that you have the following installed:

- Python 3.x
- Tkinter (comes with standard Python installations)
- OpenCV (`cv2`) library
- Tesseract OCR Engine
- pytesseract Python library
- Pillow Python library

You can install the required Python libraries using `pip`:

```bash
pip install opencv-python pytesseract pillow

git clone https://github.com/your-username/document-digitalization-app.git
cd document-digitalization-app

pip install -r requirements.txt
