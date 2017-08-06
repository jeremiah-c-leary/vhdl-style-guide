

import argparse
import sys

# Rules
sys.path.append('..\modules')
import rule_whitespace

def parse_command_line_arguments():
    '''Parses the command line arguments and returns them.'''

    parser = argparse.ArgumentParser(prog='VHDL Style Guide (VSG)',
                                     description='Analyzes VHDL files\
                                                  for style guide violations.')

    parser.add_argument('-f', '--filename', required=True)

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    else:
        return parser.parse_args()


def open_vhdl_file(commandLineArguments):
    '''This opens the VHDL file, reads it, removes ending CRLF's and LFs, and return a list.'''

    vhdlList = []

    with open(commandLineArguments.filename, 'r') as vhdlFile:
        for line in vhdlFile:
            vhdlList.append(line.strip('\n'))

    return vhdlList


def main():
    '''Main routine of the VHDL Style Guide (VSG) program.'''

    commandLineArguments = parse_command_line_arguments()
    print commandLineArguments
    vhdlList = open_vhdl_file(commandLineArguments)

    print vhdlList

if __name__ == '__main__':
    main()
