# Importing libraries #
import re, string
from unittest import result
import nltk
import numpy as np
import pandas as pd
import lightgbm as lgb

# import seaborn as sn
import language_tool_python

# import matplotlib.pyplot as plt
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import WordPunctTokenizer
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from textacy import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import sklearn.metrics as metrics
from sklearn.pipeline import Pipeline
import pickle
import os

basepath = str(os.path.abspath(os.getcwd()))


def inference_model(series, filename_model, filename_transformer):
    path_model = f"{basepath}/outputs/models/"
    path_transformer = f"{basepath}/outputs/transformers/"
    model = pickle.load(open(path_model + filename_model, "rb"))
    tfidf_vectorizer = pickle.load(open(path_transformer + filename_transformer, "rb"))
    # Vecotrizing column text using tfidf #
    test_input = tfidf_vectorizer.fit_transform(series)
    # usar predict proba # .targe value_counts() 0 y 1 - Output is a ndarray, [p0, p1] with the probability of each label
    test_pred = model.predict_proba(test_input)
    return test_pred


def get_top_5(test_pred, df):
    # asociar predicion
    i = 0
    ind = np.argpartition(test_pred[:, 1], -6)[-6:]
    probability = test_pred[:, 1][ind]
    result_inference = {}
    for value in ind:
        sentencia = df["Sentencia"][value]
        decimal_probability = int(probability[i]*100)
        result_inference[i] = {
            "probability": {decimal_probability},
            "sentencia": {sentencia},
        }
        i = i + 1
    return result_inference
