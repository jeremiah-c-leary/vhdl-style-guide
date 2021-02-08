
import subprocess
import os

try:
    from vsg import version_info
    sVersion = version_info.sVersion
    sShaNum = version_info.sShaNum
except ImportError:
    sVersion = None
    sShaNum = None

def print_version(oCommandLineArguments, sShaNum=sShaNum):

    if (oCommandLineArguments.version):

        sShaNum = get_git_sha(sVersion, sShaNum)

        print('VHDL Style Guide (VSG) version: ' + str(sVersion))

        print('Git commit SHA: ' + str(sShaNum))

        exit(0)

def get_git_sha(sVersion, sShaNum):
    if sShaNum is None and sVersion is None:
        sReturnPath = os.getcwd()
        sPath = os.path.dirname(__file__)
        os.chdir(sPath)
        lActual = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
        lActual = str(lActual.decode('utf-8')).split('\n')
        sReturn = lActual[0]
        os.chdir(sReturnPath)
    else:
        return sShaNum
    return sReturn

def get_git_branch():
    sReturnPath = os.getcwd()
    sPath = os.path.dirname(__file__)
    os.chdir(sPath)
    lActual = subprocess.check_output(['git', 'branch', '--show-current'])
    lActual = str(lActual.decode('utf-8')).split('\n')
    sReturn = lActual[0]
    os.chdir(sReturnPath)
    return sReturn
