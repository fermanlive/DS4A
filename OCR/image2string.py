import pytesseract
import os
from PIL import Image
import json
import easyocr
import time

reader = easyocr.Reader(['es']) # this needs to run only once to load the model into memory

def image2string(routefile:str):
    img = Image.open(routefile) # Abre la imagen con pillow
    img.load()
    text = pytesseract.image_to_string(img, lang='spa') # Extrae el texto de la imagen
    return text

def image2string_easyocr(routefile:str):
    result = reader.readtext(routefile)
    for resulting in result:
        return resulting[1]


def search_image(directory_str:str):
    directory = os.fsencode(directory_str)
    list_text = {}
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith("jpg"): 
            test_raw = image2string_easyocr(directory_str+'/'+filename)
            list_text[filename[:-4]]=test_raw
    return list_text