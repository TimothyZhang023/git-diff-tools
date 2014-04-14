#! /usr/bin/env python
# -*- coding: utf-8 -*-
#@author TianShuo
#@version 2014-04-13 16:57
# apply_patch 从指定文件夹覆盖并自动备份

import os
import time
import zipfile
import shutil
import sys
import common
import conf

versionDate = conf.versionDate
sourceDir = conf.sourceBaseDir + versionDate + r"\finally"
targetDir = conf.workingDir
backupDir = conf.backupBaseDir + versionDate + r"\\"
copyFileCounts = 0


def copyFiles(sourceDirs, targetDirs):
    global copyFileCounts
    print sourceDirs
    print u"%s 当前处理文件夹%s已处理%s 个文件" % (
        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), sourceDirs, copyFileCounts)
    for f in os.listdir(sourceDirs):
        sourceF = os.path.join(sourceDirs, f)
        targetF = os.path.join(targetDirs, f)

        if os.path.isfile(sourceF):
            #创建目录
            if not os.path.exists(targetDirs):
                os.makedirs(targetDirs)
            copyFileCounts += 1

            #文件不存在，或者存在但是大小不同，覆盖
            if not os.path.exists(targetF) or (
                    os.path.exists(targetF) and (os.path.getsize(targetF) != os.path.getsize(sourceF))):
                #2进制文件
                open(targetF, "wb").write(open(sourceF, "rb").read())
                print u"%s %s 复制完毕" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), targetF)
            else:
                temp_dir = sourceF.replace(sourceDir, '')
                temp_dir = backupDir + temp_dir
                if not os.path.exists(os.path.dirname(temp_dir)):
                    os.makedirs(os.path.dirname(temp_dir))
                shutil.copy(sourceF, temp_dir)

                print u"%s %s 已存在，不重复复制" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), targetF)

        if os.path.isdir(sourceF):
            copyFiles(sourceF, targetF)


if __name__ == "__main__":
    # try:
    #     import psyco
    #
    #     psyco.profile()
    # except ImportError:
    #     pass

    if not os.path.exists(backupDir):
        os.makedirs(backupDir)

    copyFiles(sourceDir, targetDir)
