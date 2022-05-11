from pdf2image import convert_from_path
import os

def pdf2image(routefile:str,filename:str):
    # Store Pdf with convert_from_path function
    images = convert_from_path(routefile)

    for i in range(len(images)):
        # Save pages as images in the pdf
        parent_dir = "output_images"
        directory = filename[:-4]
        create_dir(parent_dir,directory)
        images[i].save(f'{parent_dir}/{directory}/page'+ str(i) +'.jpg', 'JPEG') 
    return f'{directory}'

def create_dir(parent_dir:str,directory:str):
    path = os.path.join(parent_dir, directory)
    isdir = os.path.isdir(path)
    if not isdir :
        os.mkdir(path)
        

def search_pdf(directory_str:str):
    directory = os.fsencode(directory_str)
    list_images = []
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith("pdf"): 
            print(f"Ready to save the {filename}")
            route_file_image = pdf2image(directory_str+'/'+filename,filename)
            list_images.append(route_file_image)
            print(f"The {filename} was saved !!")
    return list_images

            
