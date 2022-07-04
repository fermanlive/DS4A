from fastapi import FastAPI, File
import uvicorn
from routers import orquestador
import json 
app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File()):
    path = "inputs/"
    filename = "filename.pdf"
    with open(f'{path}{filename}', "wb") as file_to_save:
        file_to_save.write(file)
    return {"message": f"the file {filename} was saved!", "filename": filename}


@app.post("/pdf_to_image/")
async def launch_pdf_to_image(filename: str):
    orquestador.pdf_2_image(filename)
    return {"message": "The images was created by the pdf file"}

@app.post("/image_to_text/")
async def image_to_text(filename: str):
    orquestador.image_2_text(filename)
    return {"message": f"the file {filename}.txt was saved!", "filename": f"{filename}.txt"}

@app.post("/inference_start/")
async def inference_start(filename: str):
    path = "output_txt/"
    with open(path+filename) as f:
        lines = f.readlines()
        lines=lines[0]
        lines = json.loads(lines)
        dictionary_file = renaming_keys(lines)
        nested_text = concat_text_sentence(dictionary_file)
        clean_text = get_clean_text(nested_text)
    return {"message": f"The text obtain {clean_text}"}


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