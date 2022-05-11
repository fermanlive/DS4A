import pytesseract

from PIL import Image

def image2string(routefile:str):
    img = Image.open(routefile) # Abre la imagen con pillow
    img.load()
    text = pytesseract.image_to_string(img, lang='spa') # Extrae el texto de la imagen
    print(text)

if __name__ == "__main__":
    image2string('output_images/page0.jpg')
    