
import subprocess
import os

try:
    from vsg import version_info
    sVersion = version_info.sVersion
    sShaNum = version_info.sShaNum
except ImportError:
    sVersion = None
    sShaNum = None

def print_version(oCommandLineArguments, sVersion=sVersion, sShaNum=sShaNum):

    if (oCommandLineArguments.version):

        sVersion, sShaNum = get_version_info(sVersion, sShaNum)

        print('VHDL Style Guide (VSG) version: ' + str(sVersion))

        print('Git commit SHA: ' + str(sShaNum))

        exit(0)

#def get_git_sha(sVersion, sShaNum):
#    try:
#        if sShaNum is None and sVersion is None:
#            sReturnPath = os.getcwd()
#            sPath = os.path.dirname(__file__)
#            os.chdir(sPath)
#            lActual = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
#            lActual = str(lActual.decode('utf-8')).split('\n')
#            sReturn = lActual[0]
#            os.chdir(sReturnPath)
#        else:
#            return sShaNum
#        return sReturn
#    except subprocess.CalledProcessError:
#        return 'Unknown'
#
#def get_git_branch():
#    try:
#        sReturnPath = os.getcwd()
#        sPath = os.path.dirname(__file__)
#        os.chdir(sPath)
#        lActual = subprocess.check_output(['git', 'branch', '--show-current'])
#        lActual = str(lActual.decode('utf-8')).split('\n')
#        sReturn = lActual[0]
#        os.chdir(sReturnPath)
#        return sReturn
#    except subprocess.CalledProcessError:
#        return 'Unknown'

def get_version_info(sVersion, sShaNum):
    if sVersion is not None and sShaNum is not None:
        return sVersion, sShaNum

    try:
        sReturnPath = os.getcwd()
        sPath = os.path.dirname(__file__)
        os.chdir(sPath)
        lActual = subprocess.check_output(['git', 'describe', '--tags'])
        lActual = str(lActual.decode('utf-8')).split('\n')
        lVersion = lActual[0].split('-')
        sVersion = str(lVersion[0]) + '.dev' + str(lVersion[1])
        sShaNum = str(lVersion[-1])
        os.chdir(sReturnPath)
        return sVersion, sShaNum
    except subprocess.CalledProcessError:
        return '0.0.0.dev0', 'unknown'
