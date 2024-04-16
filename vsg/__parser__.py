# -*- coding: utf-8 -*-
import argparse
import sys

from tests import utils

from . import config, vhdlFile
from .CustomArgumentParser import CustomArgumentParser


def parse_command_line_arguments():
    """Parses the command line arguments and returns them."""

    parser = CustomArgumentParser(prog="VHDL Style Guide (VSG) Parser", description="""Outputs the results from parsing a VHDL file.""")

    parser.add_argument("-f", "--filename", help="File to print parser output")
    parser.add_argument("-w", "--whitespace", default=False, action="store_true", help="Include whitespace objects")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    else:
        return parser.parse_args()


def main():
    """Main routine of parser output"""

    fExitStatus = 0

    commandLineArguments = parse_command_line_arguments()
    commandLineArguments.style = "indent_only"
    commandLineArguments.configuration = []
    commandLineArguments.debug = False
    commandLineArguments.fix_only = False
    commandLineArguments.stdin = False
    commandLineArguments.force_fix = False
    commandLineArguments.fix = False

    sFileName = commandLineArguments.filename

    lLines = vhdlFile.utils.read_vhdlfile(sFileName)

    configuration = config.New(commandLineArguments)

    oVhdlFile = vhdlFile.vhdlFile(lLines[0], commandLineArguments, None, None, configuration)
    oVhdlFile.filename = sFileName

    utils.print_objects(oVhdlFile, not commandLineArguments.whitespace)

    sys.exit(fExitStatus)


if __name__ == "__parser__":
    main()
