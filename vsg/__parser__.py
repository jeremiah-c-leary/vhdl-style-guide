#!/usr/bin/env python

import argparse
import sys

from . import vhdlFile

from vsg.tests import utils


def parse_command_line_arguments():
    '''Parses the command line arguments and returns them.'''

    parser = argparse.ArgumentParser(
      prog='VHDL Style Guide (VSG) Parser',
      description='''Outputs the results from parsing a VHDL file.''')

    parser.add_argument('-f', '--filename', help='File to print parser output')
    parser.add_argument('-w', '--whitespace', default=False, action='store_true', help='Include whitespace objects')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    else:
        return parser.parse_args()


def main():
    '''Main routine of parser output'''

    fExitStatus = 0

    commandLineArguments = parse_command_line_arguments()

    sFileName = commandLineArguments.filename

    oVhdlFile = vhdlFile.vhdlFile(vhdlFile.utils.read_vhdlfile(sFileName))
    oVhdlFile.filename = sFileName

    utils.print_objects(oVhdlFile, not commandLineArguments.whitespace)

    sys.exit(fExitStatus)


if __name__ == '__parser__':
    main()
