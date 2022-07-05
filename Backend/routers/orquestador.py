from routers.pdf_to_image import search_pdf
from routers.ocr import search_image
import codecs
import json
import os
basepath = str(os.path.abspath(os.getcwd()))

def pdf_2_image(filename):
    list_images = search_pdf(directory_str="inputs", filename = filename)
    return list_images 

def image_2_text(filename):
    directory_str=basepath+"/output_images/"+filename
    list_text = search_image(directory_str=directory_str)
    extension = ".txt"
    route = f'output_txt/{filename}'
    file = codecs.open(route+extension, "w+", "utf-8")
    file.write(json.dumps(list_text))
    return list_text