# Importing libraries #
import re, string
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

tool = language_tool_python.LanguageTool("es-US")
stemmer = SnowballStemmer("spanish")
nltk.download("stopwords")


def renaming_keys(lines):
    for i in range(len(lines)):
        lines[i] = lines[f"page{str(i)}"]
        del lines[f"page{str(i)}"]
    return lines


def concat_text_sentence(dictionary_file):
    nested_text = ""
    for key, value in sorted(dictionary_file.items(), key=lambda item: int(item[0])):
        nested_text = nested_text + " " + dictionary_file[key]
    return nested_text


def get_clean_text(nested_text):
    nested_text = nested_text.replace("\n", "")
    nested_text = nested_text.lower()
    import unicodedata

    nested_text_1 = nested_text.replace("ñ", "#").replace("Ñ", "%")
    clean_text = (
        unicodedata.normalize("NFKD", nested_text_1)
        .encode("ascii", "ignore")
        .decode("ascii")
        .replace("#", "ñ")
        .replace("%", "Ñ")
    )
    return clean_text


def get_list_text_subextract(
    clean_text, list_keywords_victim, before_vecindad, after_vecindad
):
    list_text_subextract = []
    for list_victims_word in list_keywords_victim:
        for m in re.finditer(list_victims_word, clean_text):
            start = int(m.start() - before_vecindad)
            end = int(m.end() + after_vecindad)
            list_text_subextract.append(clean_text[start:end])
    return list_text_subextract


# Deifining key functions #

# Preprocessing paragraphs #


def process_paragraph(paragraph):
    """
    This function removes non representative string characters
    input: paragraph extracted from plain text file
    output: paragraph withoput stopwords and punctuation
    """

    # Function for data cleaning #
    def text_cleaning(text_to_clean):
        """
        This function cleans the text data
        """
        text_to_clean = preprocessing.remove.punctuation(text_to_clean)
        text_to_clean = preprocessing.remove.accents(text_to_clean)
        text_to_clean = preprocessing.normalize.whitespace(text_to_clean)
        text_to_clean = preprocessing.normalize.unicode(text_to_clean)
        return text_to_clean

    # Function for removing stopwords #
    def stopword(string):
        a = [i for i in string.split() if i not in stopwords.words("spanish")]
        return " ".join(a)

    # Stemming the paragraph #
    def stemming(text_to_process):
        return " ".join([stemmer.stem(i) for i in text_to_process.split()])

    # Correcting the input pragraph #
    new_paragraph = stemming(stopword(text_cleaning(tool.correct(paragraph))))

    return new_paragraph
