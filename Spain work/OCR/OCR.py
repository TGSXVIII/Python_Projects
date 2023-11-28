from PIL import Image
import pytesseract

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update the path accordingly

# ------------------------------------------------------------------------------------------ #
def imageText(image, lang='eng'):
    return pytesseract.image_to_string(Image.open(image), lang=lang)
# ------------------------------------------------------------------------------------------ #

print(imageText("Pictures/img_0.png"))
print(imageText("Pictures/img_1.jpg"))

