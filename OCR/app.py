from image2string import search_image
from pdftoimage import search_pdf
import json

def main():
    list_images = search_pdf('pdf')
    for dir_images in list_images :
        text = search_image('output_images/'+dir_images)
        with open(f'ouput_txt/{dir_images}.txt',"w+") as f:
            print(f"Ready to save the text for file: {dir_images}")
            f.write(json.dumps(text))
            print(f"The {dir_images}.txt was saved !!")

if __name__ == "__main__":
    main()