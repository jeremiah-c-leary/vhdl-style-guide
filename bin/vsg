#!/usr/bin/python

import argparse
import sys
import os

# Get the path to the executable
executablePath = os.path.dirname(os.path.realpath(__file__))

# Import program modules
sys.path.append(os.path.join(executablePath,'..'))
from vsg import rule_list
from vsg import vhdlFile

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


def main():
    '''Main routine of the VHDL Style Guide (VSG) program.'''

    commandLineArguments = parse_command_line_arguments()
    oRules = rule_list.list(vhdlFile.vhdlFile(commandLineArguments.filename))
    oRules.check_rules()
    oRules.report_violations()


if __name__ == '__main__':
    main()
