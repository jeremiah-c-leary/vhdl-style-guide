
sVersion = 'master'
sShaNum = 'NA'


def print_version(oCommandLineArguments):

    if (oCommandLineArguments.version):
        print('VHDL Style Guide (VSG) version: ' + str(sVersion))

        print(f'Git commit SHA: {sShaNum}')

        exit(0)
