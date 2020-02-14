import json
import uuid
from flask import Flask, request, abort, send_file, jsonify
from flask_cors import CORS
import download


app = Flask(__name__)
app.config.from_pyfile('application.cfg', silent=True)

CORS(app, resources={r"/*": {"origins": "*"}})

download_requests = {}

@app.route('/')
def root():
    #abort(403)
    return 'API root'


@app.route('/request_download', methods = ['POST'])
def request_download():
    file_url = request.form.get('file_url')

    if file_url == None:
        abort(403)

    download_request = {
        'file_id': None,
        'file_url': file_url,
        'file_name': file_url.split('/')[-1],
        'download_progression': 0,
        'md5sum': None,
        'sha1sum': None,
        'virus_report': None,
        'vul_report': None,
        'zip_path': None,
        'zip_download_session': None,
        'zip_download_timestamp': None
    }

    # Download and zip
    download_request=download.download_md5sum_zip(download_request)

    download_requests[file_url] = download_request

    return file_url

@app.route('/get_download_state')
def get_download_state():
    file_url = request.args.get('file_url')
    return jsonify(download_requests[file_url])

@app.route('/get_download_zip')
def get_download_zip():
    file_url = request.args.get('file_url')

    download_request = download_requests[file_url]

    # zip_download_timestamp = now
    # zip_download_session += 1
    # return zip stream
    # zip_download_session -= 1
    
    # Message cleanup
    # - user_session_id
    # - file_url
    return send_file(download_request['zip_path'], attachment_filename=download_request['file_name'] + '.zip')


if __name__ == '__main__':
    app.run()