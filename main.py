# -*- coding: utf-8 -*-
# admin@zts1993.com
__author__ = 'TianShuo'

import re, os, urllib2, shutil


def run(patch_dir, project_path, out_path):
    # try:
    #     os.chdir(patch_dir)
    # except Exception, e:
    #     raise e

    files = os.listdir(patch_dir)
    for file in files:
        matchfilename = r'\d{4}-'
        order = re.findall(matchfilename, file, re.S)
        order_num = order[0]

        patch_file = patch_dir + os.sep + file
        print u'start_to_process:', patch_file
        patch = open(patch_file, 'r')
        hash_folder = ''
        while 1:
            line_content = patch.readline()
            if line_content:
                matchdiff = r'^diff --git a(.*) b(.*)\n'
                matchhash = r'^From (.*?) '

                hash = re.findall(matchhash, line_content, re.S)
                if hash:
                    hash_folder = out_path + os.sep + order_num+hash[0]

                    print u'commit hash:', hash[0]
                    print u'commit folder:', hash_folder

                    if os.path.exists(out_path) == False:
                        os.mkdir(out_path)
                        pass
                        # try:
                    #     os.chdir(out_path)
                    # except Exception, e:
                    #     raise e

                    if os.path.exists(hash_folder) == False:
                        os.mkdir(hash_folder)

                list = re.findall(matchdiff, line_content, re.S)
                if list:
                    file_now_path = project_path + list[0][0]
                    file_old_path = hash_folder + list[0][0]
                    tempdir = os.path.dirname(file_old_path)

                    if os.path.exists(tempdir) == False:
                        os.makedirs(tempdir)

                    print u'lastest file:' + file_now_path
                    print u'copy to:' + file_old_path
                    if os.path.isfile(project_path + list[0][0]):
                        shutil.copy(project_path + list[0][0], hash_folder + list[0][0])


            else:
                break


if __name__ == '__main__':
    patch_dir = r"C:\wamp\www\GreenCMS_Update\patch"
    project_path = r"C:\wamp\www\Green2014"
    out_path = r"C:\wamp\www\GreenCMS_Update"
    print patch_dir
    #date_from = "2014-01-25"
    #date_to = "2014-02-26"
    run(patch_dir, project_path, out_path)








