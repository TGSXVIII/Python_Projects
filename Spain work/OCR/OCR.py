import os
from PIL import Image
import pytesseract
from pathlib import Path
from pdf2image import convert_from_path
from tempfile import TemporaryDirectory

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update the path accordingly
poppler_path = r"C:\Users\mads020n\Desktop\poppler-23.11.0\Library\bin"

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
    file = Path(r'./Files/'+pdf)

    with TemporaryDirectory() as tempdir:
        pages = convert_from_path(file, 500, poppler_path=poppler_path)

        for page_numb, page in enumerate(pages, start=1):
            filename = f"{tempdir}/page_{page_numb}.jpg"
            page.save(Path(filename).as_posix(), "JPEG")
            page_list.append(filename)

    with open('test.txt', 'wb') as output_file:
        for page in page_list:
            output_file.write(imageText(Path(page).as_posix()).encode('utf-8'))

# ------------------------------------------------------------------------------------------ #

print(imageText("Pictures/img_0.png"))
print(imageText("Pictures/img_1.jpg"))

print(convertPdf("invoice.pdf"))

print(checkFiles("Files"))
print(checkPictures("Pictures"))

