# -*- coding: utf-8 -*-
# admin@zts1993.com
# git-tool 从指定commit生成增量更新包
__author__ = 'TianShuo'

import re
import os
import shutil
import zipfile
import subprocess


def del_folder(filename):
    if os.path.isdir(filename):
        for root, dirs, files in os.walk(filename, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
                print  os.path.join(root, name)
            for name in dirs:
                os.rmdir(os.path.join(root, name))
                print "delete %s" % (os.path.join(root, name))
        os.rmdir(filename)
    else:
        os.remove(filename)


def run(patch_dir, project_path, final_folder):
    patch_files = os.listdir(patch_dir)
    for file_name in patch_files:

        patch_file = patch_dir + os.sep + file_name
        print u'start_to_process:', patch_file
        patch_content = open(patch_file, 'r')

        while 1:
            line_content = patch_content.readline()
            if line_content:
                match_diff = r'^diff --git a(.*) b(.*)\n'

                file_list = re.findall(match_diff, line_content, re.S)

                if file_list:
                    file_now_path = project_path + file_list[0][0]
                    file_final_path = final_folder + file_list[0][0]

                    if not os.path.exists(os.path.dirname(file_final_path)):
                        os.makedirs(os.path.dirname(file_final_path))

                    print u'lastest file_name:' + file_now_path
                    print u'copy to:' + file_final_path

                    if os.path.isfile(project_path + file_list[0][0]):
                        shutil.copy(project_path + file_list[0][0], file_final_path)

            else:
                break


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


if __name__ == '__main__':
    git_hash = r'cb25c5c43683feb50da3a7d6e3679d0fefcb5ee3'

    out_path = r"C:\wamp\www\GreenCMS_Update_"+git_hash
    project_path = r"C:\wamp\www\Green2014"

    patch_dir = out_path + os.sep + 'patch'
    final_folder = out_path + os.sep + 'finally'
    zip_filename = 'upgrade.zip'

    git_path_command = r'"C:\Program Files (x86)\Git\bin\git" format-patch '
    git_path_command += git_hash
    git_path_command += r' -o "' + patch_dir + '"'

    print git_path_command

    if not os.path.exists(out_path):
        os.mkdir(out_path)

    if os.path.exists(patch_dir):
        del_folder(patch_dir)
    else:
        os.mkdir(patch_dir)

    if os.path.exists(final_folder):
        del_folder(final_folder)
    else:
        os.mkdir(final_folder)



    os.chdir(project_path)
    ps = subprocess.Popen(git_path_command)
    ps.wait()  #让程序阻塞

    run(patch_dir, project_path, final_folder)

    zip_folder(final_folder + os.sep, out_path + os.sep, zip_filename)








