from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update the path accordingly

# ------------------------------------------------------------------------------------------ #
def imageText(image, lang='eng'):
    return pytesseract.image_to_string(Image.open(image), lang=lang)
# ------------------------------------------------------------------------------------------ #

#def pdfToImage(pdf):
#    with open(pdf, "rb") as pdf:
#        pages = convert_from_bytes(pdf.read())
#        for page in pages:
#            page.save("page_image.jpg", format="jpeg")

# Open an image using PIL (Python Imaging Library)
#pdfToImage('img_2.pdf')

print(imageText("img_0.png"))
print(imageText("img_1.jpg"))
#print(imageText("page_image.jpg"))
