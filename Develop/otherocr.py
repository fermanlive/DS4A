import easyocr
import time
start_time = time.time()
reader = easyocr.Reader(['es']) # this needs to run only once to load the model into memory
result = reader.readtext('output_images/050453121001-201601732-00 Chigorodó 19 Diciembre 2017/page0.jpg')
print("--- %s seconds ---" % (time.time() - start_time))
print(type(result))
