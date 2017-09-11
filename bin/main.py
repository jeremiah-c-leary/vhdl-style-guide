

import argparse
import sys

# Rules
sys.path.append('..\modules')
import rule_list
import vhdlFile

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
    oRules = rule_list.list()
    oRules.check_rules(vhdlFile.vhdlFile(commandLineArguments.filename))
    oRules.report_violations(commandLineArguments.filename)


if __name__ == '__main__':
    main()
