import codecs
import json
import os
import pickle
from routers.ocr import search_image
from routers.pdf_to_image import search_pdf
from routers.preprocessing_features import (
    renaming_keys,
    concat_text_sentence,
    get_clean_text,
    get_list_text_subextract,
    process_paragraph,
)

from routers.inference_model import inference_model, get_top_5
import pandas as pd
import numpy as np

basepath = str(os.path.abspath(os.getcwd()))


def pdf_2_image(filename: str):
    list_images = search_pdf(directory_str="inputs", filename=filename)
    return list_images


def image_2_text(filename: str):
    directory_str = basepath + "/output_images/" + filename
    list_text = search_image(directory_str=directory_str)
    extension = ".txt"
    route = f"output_txt/{filename}"
    file = codecs.open(route + extension, "w+", "utf-8")
    file.write(json.dumps(list_text))
    return list_text


def get_complete_clean_text(filename: str):
    path = "output_txt/"
    ext_txt = ".txt"
    with open(path + filename + ext_txt) as f:
        lines = f.readlines()
        lines = lines[0]
        lines = json.loads(lines)
        dictionary_file = renaming_keys(lines)
        nested_text = concat_text_sentence(dictionary_file)
        clean_text = get_clean_text(nested_text)
    return clean_text


list_keywords = {
    "list_keywords_victimario": [
        "eln",
        "grupo armado",
        "farc",
        "elp",
        "bacrim",
        "paramilitares",
        "auc",
        "guerrilla",
        "ejército",
        "autodefensas",
        "fuerza pública",
        " acuu",
        "fuerzas armadas",
    ],
    "list_keywords_perdida": [
        "abandono",
        "despojo",
        "desplazamiento",
        "forzado",
        "tipología",
        "perdida",
    ],
    "list_keywords_solicitante": [
        "solicitante",
        "reclamante",
        "accionante",
        "demandante",
    ],
    "list_keywords_decision": [
        "restitución",
        "restituye",
        "formaliza",
        "formalización",
        "negar",
        "proteger",
        "ordenar",
        "restituir",
        "decretar",
        "amparar",
        "petición",
        "nieguese",
        "nieganse",
    ],
    "list_keywords_ubicacion": [
        "departamento",
        "municipio",
        "vereda",
        "urbano",
        "rural",
        "matricula",
        "inmobiliaria",
    ],
}


def extract_subtext(list_keywords, before_vecindad, after_vecindad, clean_text):
    list_text_subextract = []
    list_document_list_victims = get_list_text_subextract(
        clean_text, list_keywords, before_vecindad, after_vecindad
    )
    list_text_subextract.extend(list_document_list_victims)
    return list_text_subextract


def extract_features(clean_text: str):
    before_vecindad = 150
    after_vecindad = 300
    #### Victimario
    list_victimario = extract_subtext(
        list_keywords["list_keywords_victimario"],
        before_vecindad,
        after_vecindad,
        clean_text,
    )

    #### Tipologia perdida del bien
    list_perdida = extract_subtext(
        list_keywords["list_keywords_perdida"],
        before_vecindad,
        after_vecindad,
        clean_text,
    )

    #### Solicitante
    list_solicitante = extract_subtext(
        list_keywords["list_keywords_solicitante"],
        before_vecindad,
        after_vecindad,
        clean_text,
    )

    #### Sentido de la decisión
    list_decision = extract_subtext(
        list_keywords["list_keywords_decision"],
        before_vecindad,
        after_vecindad,
        clean_text,
    )

    #### Ubicación
    list_ubicacion = extract_subtext(
        list_keywords["list_keywords_ubicacion"],
        before_vecindad,
        after_vecindad,
        clean_text,
    )

    list_features = {
        "list_victimario": list_victimario,
        "list_perdida": list_perdida,
        "list_solicitante": list_solicitante,
        "list_decision": list_decision,
        "list_ubicacion": list_ubicacion,
    }

    return list_features


def inference(list_features):
    df_victimario_test = pd.DataFrame(
        list_features["list_victimario"], columns=["Sentencia"]
    )
    df_perdida_test = pd.DataFrame(list_features["list_perdida"], columns=["Sentencia"])
    df_solicitante_test = pd.DataFrame(
        list_features["list_solicitante"], columns=["Sentencia"]
    )
    df_decision_test = pd.DataFrame(
        list_features["list_decision"], columns=["Sentencia"]
    )
    df_ubicacion_test = pd.DataFrame(
        list_features["list_ubicacion"], columns=["Sentencia"]
    )

    df_victimario_test["Sentencia_cleaned"] = df_victimario_test["Sentencia"].apply(lambda x: process_paragraph(x))
    df_perdida_test["Sentencia_cleaned"] = df_perdida_test["Sentencia"].apply(
        lambda x: process_paragraph(x)
    )
    df_solicitante_test["Sentencia_cleaned"] = df_solicitante_test["Sentencia"].apply(lambda x: process_paragraph(x))
    df_decision_test["Sentencia_cleaned"] = df_decision_test["Sentencia"].apply(
        lambda x: process_paragraph(x)
    )
    df_ubicacion_test["Sentencia_cleaned"] = df_ubicacion_test["Sentencia"].apply(lambda x: process_paragraph(x))

    filename_model = "fitted_model_decision.pkl"
    filename_transformer = "transformer_model_decision.pkl"
    dict_decision = inference_model(
        df_decision_test["Sentencia_cleaned"], filename_model, filename_transformer
    )
    result_decision = get_top_5(dict_decision, df_decision_test)

    filename_model = "fitted_model_perdida.pkl"
    filename_transformer = "transformer_model_perdida.pkl"
    dict_perdida = inference_model(
        df_perdida_test["Sentencia_cleaned"], filename_model, filename_transformer
    )
    result_perdida = get_top_5(dict_perdida, df_perdida_test)

    filename_model = "fitted_model_solicitante.pkl"
    filename_transformer = "transformer_model_solicitante.pkl"
    dict_solicitante = inference_model(
        df_solicitante_test["Sentencia_cleaned"], filename_model, filename_transformer
    )
    result_solicitante = get_top_5(dict_solicitante, df_solicitante_test)

    filename_model = "fitted_model_victimario.pkl"
    filename_transformer = "transformer_model_victimario.pkl"
    dict_victimario = inference_model(
        df_victimario_test["Sentencia_cleaned"], filename_model, filename_transformer
    )
    result_victimario = get_top_5(dict_victimario, df_victimario_test)

    filename_model = "fitted_model_ubicacion.pkl"
    filename_transformer = "transformer_model_ubicacion.pkl"
    dict_ubicacion = inference_model(
        df_ubicacion_test["Sentencia_cleaned"], filename_model, filename_transformer
    )
    result_ubicacion = get_top_5(dict_ubicacion, df_ubicacion_test)

    result_features = {
        "result_decision": result_decision,
        "result_perdida": result_perdida,
        "result_solicitante": result_solicitante,
        "result_ubicacion": result_ubicacion,
        "result_victimario": result_victimario
    }

    return result_features
