import requests

url = "http://127.0.0.1:8000/files/"

payload={}
files=[
  ('file',('extracts.pdf',open('/Users/dmurcia/Downloads/extracts.pdf','rb'),'application/pdf'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)