para usar pdf2image
ubuntu apt-get install poppler-utils
mac brew install poppler

para tesseract

ubuntu
apt-get update
apt-get install libleptonica-dev tesseract-ocr tesseract-ocr-dev libtesseract-dev python3-pil tesseract-ocr-eng tesseract-ocr-script-latn

mac 
brew install tesseract

despues 
pip install tesseract
pip install tesseract-ocr

Antes de ejecutar:
chmod +x ./commands/flush_and_create.sh 
chmod +x ./commands/install.sh 

Installar depedencias 
./commands/install.sh 

Ejecutar


Docker 
``Docker build -t ocr .``

``Docker ps -a ``

Esto para obtener la información de docker image y el docker id.
Ahora la imagen que creamos es de nombre "OCR" que se encuentra delineada con la linea roja y con la linea azul el contenedor ID (CONTAINER_ID), como se puede ver en la imagen a continuación
![image docker](./images/Picture2.png)

Entonces ahora ejecutamos donde el CONTAINER_ID es el obtenido anteriormente,
`` docker cp CONTAINER_ID:./OCR/output_txt/ output_txt/  ``

deberia ser el comando de esta manera :
`` docker cp 339da2af03a0:./OCR/output_txt/ ouput_txt/  ``