import flask
import os
from google.cloud import storage
import glob
import os, sys

UPLOAD_FOLDER = './'

app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')



@app.route('/upload', methods=['POST'])
def upload_object():
    bucket_name = 'hide name'
    uploaded_files = flask.request.files.getlist("file")
    for file in uploaded_files:
        filename = os.path.basename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        source_file_name = filename
        print(source_file_name)
        destination_blob_name = filename
        upload_blob(bucket_name, source_file_name, destination_blob_name)  
    return flask.render_template("index.html")



def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"
    #client = storage.Client.from_service_account_json(json_credentials_path='credentials-python-storage.json')


    #storage_client = storage.Client()
    storage_client = storage.Client.from_service_account_json('hw4.json')

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )
    return blob.public_url

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)