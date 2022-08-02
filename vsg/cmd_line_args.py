import sys
import os
import json
import shutil
import glob
import yaml
import functools
import multiprocessing

from . import junit
from . import rule_list
from . import severity
from . import version
from . import vhdlFile
import argparse
from .CustomArgumentParser import CustomArgumentParser


def __check_strict_positive(value):
    iValue: int = int(value)
    if iValue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is an invalid value for number of jobs")
    return iValue


def __is_valid_file(value: str) -> str:
    """
    Check an argument in argparse to be a path to an existing file
    :param value: String path to analyze.
    :return:
    """
    if not os.path.isfile(value):
        raise argparse.ArgumentTypeError(f"The file {value} does not exist.")
    return value


def parse_command_line_arguments():
    """Parses the command line arguments and returns them."""

    parser = CustomArgumentParser(
        prog='VHDL Style Guide (VSG)',
        description='''Analyzes VHDL files for style guide violations.
                   Reference documentation is located at:
                   http://vhdl-style-guide.readthedocs.io/en/latest/index.html''')

    parser.add_argument('-f', '--filename', type=__is_valid_file, nargs='+', help='File to analyze')
    parser.add_argument('-lr', '--local_rules', help='Path to local rules')
    parser.add_argument('-c', '--configuration', type=__is_valid_file, nargs='+', help='JSON or YAML configuration file(s)')
    parser.add_argument('--fix', default=False, action='store_true', help='Fix issues found')
    parser.add_argument('-fp', '--fix_phase', default=7, action='store',
                        help='Fix issues up to and including this phase')
    parser.add_argument('-j', '--junit', action='store', help='Extract Junit file')
    parser.add_argument('-js', '--json', action='store', help='Extract JSON file')
    parser.add_argument('-of', '--output_format', action='store', default='vsg',
                        choices=['vsg', 'syntastic', 'summary'], help='Sets the output format.')
    parser.add_argument('-b', '--backup', default=False, action='store_true',
                        help='Creates a copy of input file for comparison with fixed version.')
    parser.add_argument('-oc', '--output_configuration', default=None, action='store',
                        help='Write configuration to file name.')
    parser.add_argument('-rc', '--rule_configuration', default=None, action='store',
                        help='Display configuration of a rule')
    parser.add_argument('--style', action='store', default=None, choices=get_predefined_styles(),
                        help='Use predefined style')
    parser.add_argument('-v', '--version', default=False, action='store_true', help='Displays version information')
    parser.add_argument('-ap', '--all_phases', default=False, action='store_true',
                        help='Do not stop when a violation is detected.')
    parser.add_argument('--fix_only', action='store', help='Restrict fixing via JSON file.')
    add_quality_report_argument(parser)
    parser.add_argument(
        "-p",
        "--jobs",
        action="store",
        default=os.cpu_count(),
        type=__check_strict_positive,
        help="number of parallel jobs to use, default is the number of cpu cores",
    )
    parser.add_argument('--debug', default=False, action='store_true', help='Displays verbose debug information')

    args_ = parser.parse_args()

    validate_backup_argument(args_)
    validate_ap_argument(args_)

    if sys.platform == "win32":
        # Work around https://bugs.python.org/issue26903
        args_.jobs = min(args_.jobs, 60)

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    else:
        return args_


def get_predefined_styles():
    '''
    Reads all predefined styles and returns a list of names.

    Parameters : None

    Returns : (list of strings)
    '''
    lReturn = []
    sStylePath = os.path.join(os.path.dirname(__file__), 'styles')
    lStyles = os.listdir(sStylePath)
    for sStyle in lStyles:
        if sStyle.endswith('.yaml'):
            with open(os.path.join(sStylePath, sStyle)) as yaml_file:
                tempConfiguration = yaml.safe_load(yaml_file)
            lReturn.append(tempConfiguration['name'])
    return lReturn


def validate_backup_argument(args_):
    '''
    The function validates the backup option is only present when the fix option is also present.
    '''
    if args_.backup and not args_.fix:
        print('ERROR:  --backup argument requires --fix argument')
        sys.exit(1)


def validate_ap_argument(args_):
    '''
    The function validates the ap option is not present when the fix option is also present.
    '''
    if args_.all_phases and args_.fix:
        print('ERROR:  -ap argument is invalid with the --fix argument')
        sys.exit(1)


def add_quality_report_argument(parser):
    parser.add_argument(
        '--quality_report',
        action='store',
        help='Create code quality report for GitLab'
    )
