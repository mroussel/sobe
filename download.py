import urllib.request
import uuid
import zip_file
import fingerprint
import os


def download_md5sum_zip(download_request):
    uuid_file = uuid.uuid5(uuid.NAMESPACE_URL, download_request['file_url'])
    
    download_request['uuid_file'] = uuid_file

    destination_path = './tmp/' + str(uuid_file)
    destination_path_temp = destination_path + '.part'

    # Cleanup
    if os.path.exists(destination_path):
        os.remove(destination_path)

    if os.path.exists(destination_path_temp):
        os.remove(destination_path_temp)

    # Download
    urllib.request.urlretrieve(download_request['file_url'], destination_path_temp)

    # Rename
    os.rename(destination_path_temp, destination_path)

    # Get fingerprint
    download_request['md5sum'] = fingerprint.get_fingerprint(destination_path)
    download_request['zip_path'] = zip_file.zip_file(destination_path, download_request['file_name'])

    os.remove(destination_path)

    return download_request