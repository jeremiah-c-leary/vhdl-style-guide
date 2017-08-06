

import argparse
import sys

def parse_command_line_arguments():

    parser = argparse.ArgumentParser(prog='VHDL Style Guide (VSG)',
                                     description='Analyzes VHDL files\
                                                  for style guide violations.')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    else:
        return parser.parse_args()


def main():
    '''Main routine of the VHDL Style Guide (VSG) program.'''

    parse_command_line_arguments()


if __name__ == '__main__':
    main()
