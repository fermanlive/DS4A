import pytesseract
import os
from PIL import Image
import json

def image2string(routefile:str):
    img = Image.open(routefile) # Abre la imagen con pillow
    img.load()
    text = pytesseract.image_to_string(img, lang='spa') # Extrae el texto de la imagen
    return text

def search_image(directory_str:str):
    directory = os.fsencode(directory_str)
    list_text = {}
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith("jpg"): 
            route_file_image = image2string(directory_str+'/'+filename)
            list_text[filename[:-4]]=route_file_image
    return list_text