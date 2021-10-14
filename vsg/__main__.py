#!/usr/bin/env python

import sys
import os
import json
import glob
import yaml
import functools
import multiprocessing

from . import apply_rules
from . import cmd_line_args
from . import config
from . import utils

from . import junit
from . import rule_list
from . import severity
from . import version
from . import vhdlFile


def generate_output_configuration(commandLineArguments, oConfig):
    '''
    Creates a configuration based on parameters passed on the command line.
    It will send the output to a file in JSON format.

    Parameters:

      commandLineArguments: (argparse object)

      configuration: (configuration dictionary)

    Returns:  Nothing
    '''
    if commandLineArguments.output_configuration:
        configuration = oConfig.dConfig
        fExitStatus = 0
        # Create empty file so it can be used to create the rule list
        oVhdlFile = vhdlFile.vhdlFile([''])
        oRules = rule_list.rule_list(oVhdlFile, oConfig.severity_list, commandLineArguments.local_rules)
        oRules.configure(oConfig)
        dOutputConfiguration = {}
        if commandLineArguments.filename:
            dOutputConfiguration['file_list'] = []
            for sFileName in commandLineArguments.filename:
                dOutputConfiguration['file_list'].append(sFileName)
        if commandLineArguments.local_rules:
            dOutputConfiguration['local_rules'] = commandLineArguments.local_rules
        dOutputConfiguration['rule'] = oRules.get_configuration()
        dOutputConfiguration['indent'] = configuration['indent']
        with open(commandLineArguments.output_configuration, 'w') as json_file:
            json.dump(dOutputConfiguration, json_file, sort_keys=True, indent=2)
        sys.exit(fExitStatus)


def display_rule_configuration(commandLineArguments, oConfig):
    '''
    Displays the configuration of a rule passed on the command line.

    Parameters:

      commandLineArguments: (argparse object)

      configuration: (configuration dictionary)

    Returns:  Nothing
    '''
    if commandLineArguments.rule_configuration:
        configuration = oConfig.dConfig
        fExitStatus = 0
        # Create empty file so it can be used to create the rule list
        oVhdlFile = vhdlFile.vhdlFile([''])
        oRules = rule_list.rule_list(oVhdlFile, oConfig.severity_list, commandLineArguments.local_rules)
        oRules.configure(oConfig)
        dOutputConfiguration = {}
        if commandLineArguments.local_rules:
            dOutputConfiguration['local_rules'] = commandLineArguments.local_rules
        dFullConfiguration = oRules.get_configuration()
        if commandLineArguments.rule_configuration in dFullConfiguration:
            dOutputConfiguration['rule'] = {}
            dOutputConfiguration['rule'][commandLineArguments.rule_configuration] = dFullConfiguration[commandLineArguments.rule_configuration]
            # Format the data for displaying
            print(json.dumps(dOutputConfiguration, indent=2))
        else:
            print('ERROR: rule ' + commandLineArguments.rule_configuration + ' was not found.')
            fExitStatus = 1
        sys.exit(fExitStatus)


def validate_files_exist_to_analyze(sName):
    if sName is None:
        print('ERROR: No file defined by the -f command line option or filename given in configuration file.')
        sys.exit(1)


def main():
    '''Main routine of the VHDL Style Guide (VSG) program.'''

    fExitStatus = 0

    commandLineArguments = cmd_line_args.parse_command_line_arguments()

    version.print_version(commandLineArguments)

    oConfig = config.New(commandLineArguments)

    # Add local rule path to system path so the rules can be loaded
    if commandLineArguments.local_rules:
        sys.path.append(os.path.abspath(commandLineArguments.local_rules))

    if commandLineArguments.junit:
        oJunitFile = junit.xmlfile(commandLineArguments.junit)
        oJunitTestsuite = junit.testsuite('vhdl-style-guide', str(0))

    generate_output_configuration(commandLineArguments, oConfig)

    display_rule_configuration(commandLineArguments, oConfig)

    validate_files_exist_to_analyze(commandLineArguments.filename)

    dJson = create_json_dictionary()

    f = functools.partial(apply_rules.apply_rules, commandLineArguments, oConfig)
    # It's easier to debug when not using multiprocessing.Pool()
    lReturn = []
    if commandLineArguments.jobs == 1:
        for iIndex, sFileName in enumerate(commandLineArguments.filename):
            fStatus, testCase, dJsonEntry, sOutputStd, sOutputErr = f((iIndex, sFileName))
            lReturn.append((fStatus, testCase, dJsonEntry))
            if sOutputStd:
                print(sOutputStd)
            if sOutputErr:
                print(sOutputErr, file=sys.stderr)

    else:
        with multiprocessing.Pool(commandLineArguments.jobs) as pool:
            for tResult in pool.imap(f, enumerate(commandLineArguments.filename)):
                fStatus, testCase, dJsonEntry, sOutputStd, sOutputErr = tResult
                lReturn.append((fStatus, testCase, dJsonEntry))
                if sOutputStd:
                    print(sOutputStd)
                if sOutputErr:
                    print(sOutputErr, file=sys.stderr)

    for tValue in lReturn:
        fStatus, testCase, dJsonEntry = tValue
        fExitStatus = fExitStatus or fStatus

        if commandLineArguments.junit:
            oJunitTestsuite.add_testcase(testCase)

        if commandLineArguments.json:
            dJson['files'].append(dJsonEntry)

    if commandLineArguments.junit:
        oJunitFile.add_testsuite(oJunitTestsuite)
        utils.write_junit_xml_file(oJunitFile)

    if commandLineArguments.json:
        with open(commandLineArguments.json, 'w') as oFile:
            oFile.write(json.dumps(dJson, indent=2))


    sys.exit(fExitStatus)


def create_json_dictionary():
    '''
    Returns a dictionary to be used when the --json option is chosen.
    '''
    dJson = {}
    dJson['files'] = []
    return dJson
