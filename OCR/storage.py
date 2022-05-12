import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'credentials/ds4a-349915-f8bcca5971e3.json'
client = storage.Client()
bucket = client.get_bucket('ds4a-tierras')

def upload_to_bucket(route:str, extension:str) -> None:
    route_bucket = route+extension
    blob = bucket.blob(route_bucket)
    blob.upload_from_filename(route_bucket)