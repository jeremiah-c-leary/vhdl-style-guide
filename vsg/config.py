
import glob
import os
import sys
import yaml

from . import junit
from . import severity
from . import utils


def read_predefined_style(sStyleName):
    '''
    Reads a predefined style file.

    Parameters :

      sStyleName : (string)

    Returns : (dictionary)
    '''
    dReturn = {}
    if sStyleName is not None:
        sFileName = os.path.join(os.path.dirname(__file__), 'styles', sStyleName + '.yaml')
        dReturn = open_configuration_file(sFileName)
    return dReturn


def open_configuration_file(sFileName, sJUnitFileName=None):
    '''Attempts to open a configuration file and read it's contents.'''
    try:
        with open(sFileName) as yaml_file:
            tempConfiguration = yaml.full_load(yaml_file)
    except OSError as e:
        print(f'ERROR: encountered {e.__class__.__name__}, {e.args[1]} while opening configuration file: ' + sFileName)
        write_invalid_configuration_junit_file(sFileName, sJUnitFileName)
        sys.exit(1)
    except (yaml.parser.ParserError, yaml.scanner.ScannerError) as e:
        print('ERROR: Invalid configuration file: ' + sFileName)
        print(e)
        write_invalid_configuration_junit_file(sFileName, sJUnitFileName)
        sys.exit(1)
    return tempConfiguration


def validate_file_exists(sFilename, sConfigName):
    '''Validates a file exist while using the glob function to expand filenames.'''
    if isinstance(sFilename, dict):
        sExpandedFilename = list(sFilename.keys())[0]
    else:
        sExpandedFilename = sFilename
#    print(sExpandedFilename)
    lFileNames = glob.glob(utils.expand_filename(sExpandedFilename), recursive=True)
#    print(lFileNames)
    if len(lFileNames) == 0:
        print('ERROR: Could not find file ' + sFilename + ' in configuration file ' + sConfigName)
        sys.exit(1)


def read_configuration_files(dStyle, commandLineArguments):
    dConfiguration = dStyle
    if commandLineArguments.configuration:
        for sConfigFilename in commandLineArguments.configuration:
            tempConfiguration = open_configuration_file(sConfigFilename, commandLineArguments.junit)

            for sKey in tempConfiguration.keys():
                if sKey == 'file_list':
                    if 'file_list' not in dConfiguration:
                        dConfiguration['file_list'] = []
                    for iIndex, sFilename in enumerate(tempConfiguration['file_list']):
                        validate_file_exists(sFilename, sConfigFilename)
                        try:
                            for sGlobbedFilename in glob.glob(utils.expand_filename(sFilename), recursive=True):
                                dConfiguration['file_list'].append(sGlobbedFilename)
                        except TypeError:
                            sKey = list(sFilename.keys())[0]
                            for sGlobbedFilename in glob.glob(utils.expand_filename(sKey), recursive=True):
                                dTemp = {}
                                dTemp[sGlobbedFilename] = {}
                                dTemp[sGlobbedFilename].update(tempConfiguration['file_list'][iIndex][sKey])
                                dConfiguration['file_list'].append(dTemp)

                elif sKey == 'rule':
                    for sRule in tempConfiguration[sKey]:
                        try:
                            dConfiguration[sKey][sRule] = tempConfiguration[sKey][sRule]
                        except KeyError:
                            dConfiguration[sKey] = {}
                            dConfiguration[sKey][sRule] = tempConfiguration[sKey][sRule]
                else:
                    dConfiguration[sKey] = tempConfiguration[sKey]

    return dConfiguration


def write_invalid_configuration_junit_file(sFileName, sJUnitFileName):
    if sJUnitFileName:
        oJunitFile = junit.xmlfile(sJUnitFileName)
        oJunitTestsuite = junit.testsuite('vhdl-style-guide', str(0))
        oJunitTestcase = junit.testcase(sFileName, str(0), 'failure')
        oFailure = junit.failure('Failure')
        oFailure.add_text('Invalid JSON format.  Review configuration for errors.')
        oJunitTestcase.add_failure(oFailure)
        oJunitTestsuite.add_testcase(oJunitTestcase)
        oJunitFile.add_testsuite(oJunitTestsuite)
        utils.write_junit_xml_file(oJunitFile)


def add_debug_to_configuration(oCLA, dConfiguration):
    '''
    Adds debug values to the configuration dictionary for later use.

    Parameters:

      oCLA: (command line argument object)

      dConfiguration: (dictionary)

    Returns:  Nothing
    '''
    try:
        dConfiguration['debug'] = oCLA.debug
    except TypeError:
        dConfiguration = {}
        dConfiguration['debug'] = oCLA.debug
    return dConfiguration


def read_indent_configuration(dConfiguration):
    '''
    Reads the default indent dictionary and merges any changes from a user configuration.

    Parameters:

       dConfiguration: (dictionary)

    Returns:  (dictionary)
    '''

    sFileName = os.path.join(os.path.dirname(__file__), 'vhdlFile', 'indent', 'indent_config.yaml')

    dReturn = open_configuration_file(sFileName)

    ### This merges an indent configuration into the base indent dictionary
    if 'indent' in list(dConfiguration.keys()):
        dGroups = dConfiguration['indent']['tokens']
        for sGroup in list(dGroups.keys()):
            for sToken in list(dGroups[sGroup].keys()):
                for sParameter in list(dGroups[sGroup][sToken].keys()):
                    dReturn['indent']['tokens'][sGroup][sToken][sParameter] = dGroups[sGroup][sToken][sParameter]

    dConfiguration['indent'] = dReturn['indent']

    return dReturn


def New(commandLineArguments):
    oReturn = config()

    dStyle = read_predefined_style(commandLineArguments.style)
    dConfig = read_configuration_files(dStyle, commandLineArguments)

    oSeverityList = severity.create_list(dConfig)
    dConfig['severity_list'] = oSeverityList

    oReturn.dConfig = dConfig

    dIndent = read_indent_configuration(dConfig)
    oReturn.dIndent = dIndent

    if commandLineArguments.fix_only:
        oReturn.dFixOnly = open_configuration_file(commandLineArguments.fix_only)
    else:
        oReturn.dFixOnly = None

    return oReturn


class config():

    def __init__(self):
        dIndent = None
        dConfig = None
        dFixOnly = None
        severity_list = None
