
import os


def installing_from_git_repo():
    sPath = os.path.dirname(__file__)
    if os.path.isdir(os.path.join(sPath, '..', '.git')):
        return True
    return False


def create_version_info_file(sVersion, sShaNum):
    sVersionInfoFileName = os.path.join(os.path.dirname(__file__), 'version_info.py')

    lVersionInfo = []
    lVersionInfo.append('sVersion = \'' + str(sVersion) + "'")
    lVersionInfo.append('sShaNum = \'' + str(sShaNum) + "'")

    with open(sVersionInfoFileName, 'w') as oFile:
        for sLine in lVersionInfo:
            oFile.write(sLine + '\n')
    oFile.close()
