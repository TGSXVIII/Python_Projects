import os
import fitz
import pytesseract
from PIL import Image
from pathlib import Path
from pdf2image import convert_from_path
from tempfile import TemporaryDirectory

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
poppler_path = r'C:\Users\mads020n\Desktop\poppler-23.11.0\Library\bin'

# ------------------------------------------------------------------------------------------ #

# Take an image and convert it to text
def imageText(image, lang='eng'):
    print(image)

    if os.path.exists(image):
        return pytesseract.image_to_string(Image.open(image), lang=lang)
    else:

        print(f"File not found: {image}")
        return ""

# ------------------------------------------------------------------------------------------ #

# Check Files Directory for PDF Files and other files
def checkFiles():
    files = os.listdir("Files")

    for file in files:

        if file.endswith(".pdf"):
            convertPdf(file)
        else:
            imageText(file)

# ------------------------------------------------------------------------------------------ #

# Check Pictures Directory for PDF Files and other files
def checkPictures():
    files = os.listdir("Pictures")

    for file in files:

        if file.endswith(".pdf"):
            convertPdf(file)
        else:
            imageText(file)

# ------------------------------------------------------------------------------------------ #

def convertPdf(pdf):
    page_list = []
    file = Path('./Files') / pdf

    # Print the absolute path for debugging
    print(Path(file))

    with TemporaryDirectory() as tempdir:
        try:
            pdf_document = fitz.open(file)

            for page in range(pdf_document):
                page = pdf_document
                image = page.get_pixmap()

                # Use a unique name for each image based on the PDF filename and page number
                filename = f"{tempdir}/{pdf}.png"

                # Save the image using Pillow
                Image.frombytes("RGB", [image.width, image.height], image.samples).save(filename)
                page_list.append(filename)

        except Exception as e:
            print(f"Error converting PDF: {e}")
            return

    with open('test.txt', 'wb') as output_file:

        for page in page_list:
            image_path = Path(page)
            output_file.write(imageText(image_path).encode('utf-8'))

# ------------------------------------------------------------------------------------------ #

print(imageText("Pictures/img_0.png"))
print(imageText("Pictures/img_1.jpg"))
print(convertPdf("Invoice.pdf"))
