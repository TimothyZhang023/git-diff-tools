__author__ = 'TianShuo'
import common
import conf


if __name__ == "__main__":
    versionDate = conf.versionDate
    backupDir = conf.backupDir
    workingDir = conf.workingDir
    zip_filename = conf.versionDate + "_full.zip"

    common.zip_folder(workingDir, backupDir, zip_filename)