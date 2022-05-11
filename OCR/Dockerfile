FROM python:3.8

WORKDIR /OCR

COPY  . /OCR

RUN apt-get update
## flag -y is for said yes
RUN apt-get install poppler-utils -y
RUN apt-get install tesseract-ocr -y
RUN apt-get install libtesseract-dev -y
RUN apt-get install tesseract-ocr-spa -y

RUN python3 -m pip install -U pip

RUN pip install -r requirements.txt


#RUN python3 app.py
