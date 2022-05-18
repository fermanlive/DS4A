from image2string import search_image
from pdftoimage import search_pdf
import json
from storage import upload_to_bucket,download
import sys
from variables.list_images import list_images
import os
import shutil
import codecs


def convert_ocr_gcp():
    """
    """
    list_images = search_pdf('pdf')
    for dir_images in list_images :
        text = search_image('output_images/'+dir_images)
        route = f'output_txt/{dir_images}'
        extension = ".txt"
        print(f"Ready to save the text for file: {dir_images}")
        file = codecs.open(route+extension, "w+", "utf-8")
        file.write(json.dumps(text))
        print(f"The {dir_images}.txt was saved !!")
        upload_to_bucket(route,extension)

def download_ocr_gcp(list_images: list) -> None:
    """
    """
    for dir_images in list_images :
        download(dir_images)
        dir_images = dir_images[14:]
        text = search_image('output_images/'+dir_images)
        route = f'output_txt/{dir_images}'
        extension = ".txt"
        with open(route+extension,"w+") as f:
            print(f"Ready to save the text for file: {dir_images}")
            print('text: ', text)
            json_result = json.dumps(text)
            print('json_result: ', json_result)
            f.write(json_result)
            print(f"The {dir_images}.txt was saved !!")
        upload_to_bucket(route,extension)
        shutil.rmtree('output_images/'+dir_images)
        print(f"The {dir_images} was delete !!")


if __name__ == "__main__":
    download_ocr_gcp(list_images)