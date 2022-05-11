# import module
from pdf2image import convert_from_path
 

def pdf2image(routefile:str):
    # Store Pdf with convert_from_path function
    images = convert_from_path(routefile)
    
    for i in range(len(images)):
    
        # Save pages as images in the pdf
        images[i].save('output_images/page'+ str(i) +'.jpg', 'JPEG') 

if __name__ == "__main__":
    pdf2image('pdf/example.pdf')