FROM python:3.8

WORKDIR /OCR

COPY  . /OCR

RUN apt-get install poppler-utils
RUN apt-get update
RUN apt-get install libleptonica-dev tesseract-ocr tesseract-ocr-dev libtesseract-dev python3-pil tesseract-ocr-eng tesseract-ocr-script-latn

RUN python3 -m pip install -U pip

RUN pip install -r requirements.txt


RUN python3 app.py
