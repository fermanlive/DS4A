from os.path import join, isdir, isfile, basename
from google.cloud import storage
from os import makedirs
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'credentials/ds4a-349915-9d1624348062.json'
client = storage.Client()
bucket = client.get_bucket('ds4a-tierras')

def upload_to_bucket(route:str, extension:str) -> None:
    route_bucket = route+extension
    blob = bucket.blob(route_bucket)
    blob.upload_from_filename(route_bucket)


def download(route:str) -> None:
    bucket_name = 'ds4a-tierras'
    #prefix = 'output_images/050453121001-201500222-00 Chigorodo 8 octubre 2018'
    #dl_dir = 'output_images/050453121001-201500222-00 Chigorodo 8 octubre 2018'
    prefix = route
    dl_dir = route[14:]
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=prefix)  # Get list of files
    
    if isdir(prefix) is False:
        makedirs(prefix)

    for blob in blobs:
        if blob.name[-3:] == 'jpg' or blob.name[-3:] == 'txt':
            blob_name = blob.name
            dst_file_name = blob_name.replace('FOLDER1/FOLDER2', dl_dir)
            blob.download_to_filename(dst_file_name)  # Download

if __name__ == "__main__":
    download()