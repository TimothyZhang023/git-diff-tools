import os
import zipfile

__author__ = 'TianShuo'


def zip_folder(files_folder, out_path, zip_filename):
    cwd = files_folder
    start = cwd.rfind(os.sep) + 1
    z = zipfile.ZipFile(out_path + zip_filename, mode="w", compression=zipfile.ZIP_DEFLATED)
    try:
        for dirpath, dirs, files in os.walk(cwd):
            for file in files:
                z_path = os.path.join(dirpath, file)
                z.write(z_path, z_path[start:])
        z.close()
    finally:
        if z:
            z.close()
