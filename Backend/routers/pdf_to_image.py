import os

from pdf2image import convert_from_path

basepath = str(os.path.abspath(os.getcwd()))


def pdf_2_image(routefile: str, filename: str):
    # Store Pdf with convert_from_path function
    images = convert_from_path(basepath + "/" + routefile)

    for i in range(len(images)):
        # Save pages as images in the pdf
        parent_dir = basepath + "/output_images"
        directory = filename[:-4]
        create_dir(parent_dir, directory)
        route = f"{parent_dir}/{directory}/page" + str(i)
        extension = ".jpg"
        images[i].save(route + extension, "JPEG")
        # upload_to_bucket(route,extension)
    return f"{directory}"


def create_dir(parent_dir: str, directory: str):
    path = os.path.join(parent_dir, directory)
    isdir = os.path.isdir(path)
    if not isdir:
        os.mkdir(path)


def search_pdf(directory_str: str, filename: str):
    list_images = []
    if filename.endswith("pdf"):
        print(f"Ready to save the {filename}")
        route_file_image = pdf_2_image(directory_str + "/" + filename, filename)
        list_images.append(route_file_image)
        print(f"The {filename} was saved !!")
    return list_images
