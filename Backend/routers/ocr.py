import pytesseract
import os
from PIL import Image
import json
# import easyocr
import time

# reader = easyocr.Reader(['es']) # this needs to run only once to load the model into memory

def image2string(routefile:str):
    img = Image.open(routefile) # Abre la imagen con pillow
    img.load()
    text = pytesseract.image_to_string(img, lang='spa') # Extrae el texto de la imagen
    return text

# def image2string_easyocr(routefile:str):
#     result = reader.readtext(routefile)
#     for resulting in result:
#         return resulting[1]

def search_image(directory_str:str):
    directory = os.fsencode(directory_str)
    list_text = {}
    i = 1
    start = time.time()
    for file in os.listdir(directory):
        start_inside= time.time()
        filename = os.fsdecode(file)
        print(f'Getting text for {filename}')
        if filename.endswith("jpg"): 
            test_raw = image2string(directory_str+'/'+filename)
            list_text[filename[:-4]]=test_raw
        print(f'Text was getting {filename}')
        print(f'Ready part {i}/{len(os.listdir(directory))}')
        end_inside = time.time()
        print(f'Time for page {i} was {end_inside - start_inside}')
        i = i + 1
    end = time.time()
    time_finished_script= end - start
    print(f"Time finished all text {time_finished_script}")
    return list_text