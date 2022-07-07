import json
import os
import time

import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from routers import orquestador

basepath = str(os.path.abspath(os.getcwd()))

from fastapi import FastAPI, File

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/files/")
async def create_file(file: bytes = File()):
    start_preprocessing = time.time()
    ####Preprocesamiento texto
    path = basepath + "/inputs/"
    ext_pdf = ".pdf"
    filename = "filename"
    with open(f"{path}{filename+ext_pdf}", "wb") as file_to_save:
        file_to_save.write(file)
    launch_pdf_to_image(filename=filename + ext_pdf)
    image_to_text(filename=filename)
    clean_text = orquestador.get_complete_clean_text(filename=filename)
    list_features = orquestador.extract_features(clean_text)
    end_preprocessing = time.time()

    ####Preprocesamiento para el modelo y vectorizacion
    start_inference = time.time()
    result = orquestador.inference(list_features)
    end_inference = time.time()
    inference_time = int(end_inference - start_inference)
    time_processes_file = int(end_preprocessing - start_preprocessing)
    metrics = {"time_processes_file": time_processes_file,"inference_time":inference_time}
    os.system("./commands/flush_and_create.sh")
    message = generate_metrics()
    # return list_features
    return {"message": "The process was sucesfully", "result_inference" : result , "metrics": metrics}


def generate_metrics():
    metrics = {"time_processes_file": 100, "inference_time": 300, "time_updated": 300}
    victimary = {"AUC": 0.9, "Farc": 0.4, "ELN": 0.1}
    desition = {"Aprobada": 0.44, "aprobado y restituida": 0.11}
    motivo = {"abandono": 0.21, "abandono y retoma": 0.11}
    values = {"victimary": victimary, "desition": desition, "motivo": motivo}
    return {
        "message": "The process was sucesfully",
        "values": values,
        "metrics": metrics,
    }


def launch_pdf_to_image(filename: str):
    orquestador.pdf_2_image(filename)
    return {"message": "The images was created by the pdf file"}


def image_to_text(filename: str):
    orquestador.image_2_text(filename)
    return {
        "message": f"the file {filename}.txt was saved!",
        "filename": f"{filename}.txt",
    }


if __name__ == "__main__":
    uvicorn.run(app)
