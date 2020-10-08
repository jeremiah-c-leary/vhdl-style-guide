version = '2.2.0'

import subprocess

def print_version(oCommandLineArguments):

    if (oCommandLineArguments.version):
        print('VHDL Style Guide (VSG) version ' + str(version))

        print(retrieve_git_sha())

        exit(0)


def retrieve_git_sha():

        try:
            sShaNum = subprocess.check_output(['git', 'log', '--pretty=%h', '-n', '1'], stderr=subprocess.STDOUT)
            sShaNum = sShaNum.decode('utf-8').strip()
            return f'Git commit SHA: {sShaNum}'
        except subprocess.CalledProcessError:
            return ''
