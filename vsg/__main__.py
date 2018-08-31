#!/usr/bin/env python

import argparse
import sys
import os
import json
import shutil

from . import rule_list
from . import vhdlFile
from . import junit

def parse_command_line_arguments():
    '''Parses the command line arguments and returns them.'''

    parser = argparse.ArgumentParser(
      prog='VHDL Style Guide (VSG)',
      description='''Analyzes VHDL files for style guide violations.
                   Reference documentation is located at:
                   http://vhdl-style-guide.readthedocs.io/en/latest/index.html''')

    parser.add_argument('-f', '--filename', nargs='+', help='File to analyze')
    parser.add_argument('-lr', '--local_rules', help='Path to local rules')
    parser.add_argument('-c', '--configuration', help='JSON configuration file')
    parser.add_argument('--fix', default=False, action='store_true', help='Fix issues found')
    parser.add_argument('-fp', '--fix_phase', default=10, action='store', help='Fix issues up to and including this phase')
    parser.add_argument('-j', '--junit', action='store', help='Extract Junit file')
    parser.add_argument('-of', '--output_format', action='store', default='vsg', choices=['vsg', 'syntastic'], help='Sets the output format.')
    parser.add_argument('-b', '--backup', default=False, action='store_true', help='Creates copy of input file for comparison with fixed version.')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    else:
        return parser.parse_args()


def read_configuration_file(commandLineArguments):
    if commandLineArguments.configuration:
        with open(commandLineArguments.configuration) as json_file:
            return json.load(json_file)


def write_vhdl_file(oVhdlFile):
    with open(oVhdlFile.filename, 'w') as oFile:
        for oLine in oVhdlFile.lines[1:]:
            oFile.write(oLine.line + '\n')
    oFile.close()


def write_junit_xml_file(oJunitFile):
    with open(oJunitFile.filename, 'w') as oFile:
        for sLine in oJunitFile.build_junit():
            oFile.write(sLine + '\n')
    oFile.close()


def update_command_line_arguments(commandLineArguments, configuration):
    if configuration:
        if 'file_list' in configuration:
            for sFilename in configuration['file_list']:
                try:
                    commandLineArguments.filename.append(expand_filename(sFilename))
                except:
                    commandLineArguments.filename = [expand_filename(sFilename)]
        if 'local_rules' in configuration:
            commandLineArguments.local_rules = expand_filename(configuration['local_rules'])


def expand_filename(sFileName):
    '''Expands environment variables in filenames.'''
    return os.path.expanduser(os.path.expandvars(sFileName))


def create_backup_file(sFileName):
    '''Copies existing file and adds .bak to the end.'''
    shutil.copy2(sFileName, sFileName + '.bak')


def main():
    '''Main routine of the VHDL Style Guide (VSG) program.'''

    commandLineArguments = parse_command_line_arguments()

    configuration = read_configuration_file(commandLineArguments)

    update_command_line_arguments(commandLineArguments, configuration)

    # Add local rule path to system path so the rules can be loaded
    if commandLineArguments.local_rules:
        sys.path.append(os.path.abspath(commandLineArguments.local_rules))
    if commandLineArguments.junit:
        oJunitFile = junit.xmlfile(commandLineArguments.junit)
        oJunitTestsuite = junit.testsuite('vhdl-style-guide', str(0))
    for sFileName in commandLineArguments.filename:
        oVhdlFile = vhdlFile.vhdlFile(sFileName)
        oRules = rule_list.rule_list(oVhdlFile, commandLineArguments.local_rules)
        oRules.configure(configuration)


        if commandLineArguments.fix:
            if commandLineArguments.backup:
                create_backup_file(sFileName)
            oRules.fix(commandLineArguments.fix_phase)
            write_vhdl_file(oVhdlFile)

        oRules.check_rules()
        oRules.report_violations(commandLineArguments.output_format)

        if commandLineArguments.junit:
            oJunitTestsuite.add_testcase(oRules.extract_junit_testcase(sFileName))

    if commandLineArguments.junit:
        oJunitFile.add_testsuite(oJunitTestsuite)
        write_junit_xml_file(oJunitFile)


if __name__ == '__main__':
    main()
