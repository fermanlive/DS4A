from fastapi import FastAPI, File
import uvicorn
from routers import orquestador
import json 
import time
import os

basepath = str(os.path.abspath(os.getcwd()))

app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File()):
    start_preprocessing = time.time()
    path = basepath+"/inputs/"
    ext_pdf = ".pdf"
    filename = "filename"
    with open(f'{path}{filename+ext_pdf}', "wb") as file_to_save:
        file_to_save.write(file)
    launch_pdf_to_image(filename=filename+ext_pdf)
    image_to_text(filename=filename)
    clean_text = inference_start(filename=filename)
    end_preprocessing = time.time()
    time_processes_file = int(end_preprocessing-start_preprocessing)
    metrics = {"time_processes_file": time_processes_file}
    os.system('./commands/flush_and_create.sh')
    return {"message": "The process was sucesfully", "text" : clean_text , "metrics": metrics}

def launch_pdf_to_image(filename: str):
    orquestador.pdf_2_image(filename)
    return {"message": "The images was created by the pdf file"}

def image_to_text(filename: str):
    orquestador.image_2_text(filename)
    return {"message": f"the file {filename}.txt was saved!", "filename": f"{filename}.txt"}

def inference_start(filename: str):
    path = "output_txt/"
    ext_txt = ".txt"
    with open(path+filename+ext_txt) as f:
        lines = f.readlines()
        lines=lines[0]
        lines = json.loads(lines)
        dictionary_file = renaming_keys(lines)
        nested_text = concat_text_sentence(dictionary_file)
        clean_text = get_clean_text(nested_text)
    return clean_text


def renaming_keys(lines):
    for i in range(len(lines)):
        lines[i] = lines[f"page"+str(i)]
        del lines[f"page"+str(i)]
    return lines

def concat_text_sentence(dictionary_file):
    nested_text = ""
    for key, value in sorted(dictionary_file.items(), key=lambda item: int(item[0])):
        nested_text = nested_text+" "+dictionary_file[key] 
    return nested_text

def get_clean_text(nested_text):
    nested_text = nested_text.replace('\n', '')
    nested_text = nested_text.lower()
    import unicodedata
    nested_text_1 = nested_text.replace("ñ", "#").replace("Ñ", "%")
    clean_text = unicodedata.normalize("NFKD", nested_text_1)\
        .encode("ascii","ignore").decode("ascii")\
        .replace("#", "ñ").replace("%", "Ñ")
    return clean_text

if __name__ == "__main__":
    uvicorn.run(app)