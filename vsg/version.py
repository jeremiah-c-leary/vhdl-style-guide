
import subprocess
import os

sVersion = '3.3.0'

try:
    from vsg import version_info
    try:
        sVersion = version_info.sVersion
    except AttributeError:
        pass
    sShaNum = version_info.sShaNum
except ImportError:
    sShaNum = None


def print_version(oCommandLineArguments, sVersion=sVersion, sShaNum=sShaNum):

    if (oCommandLineArguments.version):

        sVersion, sShaNum = get_version_info(sVersion, sShaNum)

        print('VHDL Style Guide (VSG) version: ' + str(sVersion))

        print('Git commit SHA: ' + str(sShaNum))

        exit(0)

def get_version_info(sVersion, sShaNum):

    if sVersion is not None and sShaNum is not None:
        return sVersion, sShaNum

    sReturnPath = os.getcwd()
    sPath = os.path.dirname(__file__)
    if not os.path.isdir(os.path.join(sPath, '..', '.git')):
        return sVersion + '+zip.file', 'Unknown.  Installed via zip file.'

    try:
        os.chdir(sPath)
        lActual = subprocess.check_output(['git', 'describe', '--tags'])
        lActual = str(lActual.decode('utf-8')).split('\n')
        lVersion = lActual[0].split('-')
        try:
            sVersion = str(lVersion[0]) + '.dev' + str(lVersion[1])
            sShaNum = str(lVersion[-1])
        except IndexError:
            sVersion = str(lVersion[0])
        os.chdir(sReturnPath)
        return sVersion, sShaNum
    except subprocess.CalledProcessError:
        os.chdir(sReturnPath)
        return sVersion + '+zip.file', 'Unknown.  Installed via zip file.'
