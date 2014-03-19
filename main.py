# -*- coding: utf-8 -*-
# admin@zts1993.com
__author__ = 'TianShuo'

import re, os, shutil


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


if __name__ == '__main__':
    out_path = r"C:\wamp\www\GreenCMS_Update"

    project_path = r"C:\wamp\www\Green2014"

    patch_dir = out_path + os.sep + 'patch'
    final_folder = out_path + os.sep + 'finally'

    if not os.path.exists(patch_dir):
        #todo ....error
        pass

    if not os.path.exists(final_folder):
        os.mkdir(final_folder)

    run(patch_dir, project_path, final_folder)








