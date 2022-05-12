from distutils import extension
from image2string import search_image
from pdftoimage import search_pdf
import json
from storage import upload_to_bucket

def main():
    list_images = search_pdf('pdf')
    for dir_images in list_images :
        text = search_image('output_images/'+dir_images)
        route = f'ouput_txt/{dir_images}'
        extension = ".txt"
        with open(route+extension,"w+") as f:
            print(f"Ready to save the text for file: {dir_images}")
            f.write(json.dumps(text))
            print(f"The {dir_images}.txt was saved !!")
        upload_to_bucket(route,extension)


if __name__ == "__main__":
    main()