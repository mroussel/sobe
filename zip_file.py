import zipfile
import os

def zip_file(file_path, file_name):
    zf = zipfile.ZipFile(file_path + '.part' , mode='w')
    try:        
        zf.write(file_path, file_name)
    finally:
        zf.close()

    os.rename(file_path + '.part', file_path + '.zip')

    return file_path + '.zip'