
import subprocess
import os

sVersion = '3.12.1'


def print_version(oCommandLineArguments):

    if (oCommandLineArguments.version):

        sVersion, sShaNum = get_version_info()

        print('VHDL Style Guide (VSG) version: ' + str(sVersion))

        print('Git commit SHA: ' + str(sShaNum))

        exit(0)


def get_version_info():

    sVersion = '3.12.1'

    if reporting_from_zip_file():
        return sVersion + '+zip.file', 'Unknown.  Installed via zip file.'

    if installed():
        from vsg import version_info
        return version_info.sVersion, version_info.sShaNum

    if reporting_from_git_repo():
        sReturnPath = os.getcwd()
        sPath = os.path.dirname(__file__)
        os.chdir(sPath)
        lActual = subprocess.check_output(['git', 'describe', '--tags'])
        lActual = str(lActual.decode('utf-8')).split('\n')
        lVersion = lActual[0].split('-')
        try:
            sVersion = str(lVersion[0]) + '.dev' + str(lVersion[1])
            sShaNum = str(lVersion[-1][1:])
        except IndexError:
            sVersion = str(lVersion[0])
            lActual = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'])
            lActual = str(lActual.decode('utf-8')).split('\n')
            sShaNum = str(lActual[0])
        os.chdir(sReturnPath)
        return sVersion, sShaNum


def reporting_from_git_repo():
    sPath = os.path.dirname(__file__)
    if os.path.isdir(os.path.join(sPath, '..', '.git')):
        return True
    return False


def installed():
    if not reporting_from_git_repo() and version_info_file_exists():
        return True
    return False


def reporting_from_zip_file():
    if not reporting_from_git_repo() and not installed():
        return True
    return False


def version_info_file_exists():
    sVersionInfoFileName = os.path.join('vsg', 'version_info.py')
    return os.path.exists(sVersionInfoFileName)
