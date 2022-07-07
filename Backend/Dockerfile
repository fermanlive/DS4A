FROM python:3.8

RUN apt-get update
RUN apt install poppler-utils -y
RUN apt-get install tesseract-ocr -y
RUN apt-get install libtesseract-dev -y
RUN apt-get install tesseract-ocr-spa -y
RUN apt install default-jre -y
WORKDIR /ds4a

COPY  . /ds4a

RUN python3 -m pip install -U pip
RUN python3 -m pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
