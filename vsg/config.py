# -*- coding: utf-8 -*-

import glob
import os
import re
import sys

import yaml

from . import exceptions, junit, severity, utils


def read_predefined_style(sStyleName):
    """
    Reads a predefined style file.

    Parameters :

      sStyleName : (string)

    Returns : (dictionary)
    """
    dReturn = {}
    if sStyleName is not None:
        sFileName = os.path.join(os.path.dirname(__file__), "styles", sStyleName + ".yaml")
        dReturn = open_configuration_file(sFileName)
    return dReturn


def open_configuration_file(sFileName, sJUnitFileName=None):
    """Attempts to open a configuration file and read its contents."""
    try:
        with open(sFileName) as yaml_file:
            dTemp = yaml.full_load(yaml_file)
            check_for_deprecated_rule_options(dTemp, sFileName)
            return dTemp
    except OSError as e:
        print(f"ERROR: encountered {e.__class__.__name__}, {e.args[1]} while opening configuration file: " + sFileName)
        write_invalid_configuration_junit_file(sFileName, sJUnitFileName)
        sys.exit(1)
    except (yaml.parser.ParserError, yaml.scanner.ScannerError) as e:
        print("ERROR: Invalid configuration file: " + sFileName)
        print(e)
        write_invalid_configuration_junit_file(sFileName, sJUnitFileName)
        sys.exit(1)
    except exceptions.ConfigurationError as e:
        print(e.message)
        sys.exit(1)


def validate_file_exists(sFilename, sConfigName):
    """Validates a file exist while using the glob function to expand filenames."""
    if isinstance(sFilename, dict):
        sExpandedFilename = list(sFilename.keys())[0]
    else:
        sExpandedFilename = sFilename
    lFileNames = glob.glob(utils.expand_filename(sExpandedFilename), recursive=True)
    if len(lFileNames) == 0:
        print("ERROR: Could not find file " + sFilename + " in configuration file " + sConfigName)
        sys.exit(1)


def read_configuration_files(dStyle, commandLineArguments):
    if not commandLineArguments.configuration:
        return dStyle

    dConfiguration = dStyle
    lMessages = []
    for sConfigFilename in commandLineArguments.configuration:
        tempConfiguration = open_configuration_file(sConfigFilename, commandLineArguments.junit)
        dConfiguration = process_config_file(dConfiguration, tempConfiguration, sConfigFilename)
    return dConfiguration


def process_config_file(dConfiguration, tempConfiguration, sConfigFilename):
    dReturn = dConfiguration
    for sKey in tempConfiguration.keys():
        if sKey == "file_list":
            dReturn = process_file_list_key(dReturn, tempConfiguration, sKey, sConfigFilename)

        elif sKey == "rule":
            for sRule in tempConfiguration[sKey]:
                try:
                    dReturn[sKey][sRule] = tempConfiguration[sKey][sRule]
                except KeyError:
                    dReturn[sKey] = {}
                    dReturn[sKey][sRule] = tempConfiguration[sKey][sRule]
        else:
            dReturn[sKey] = tempConfiguration[sKey]
    return dReturn


dDeprecatedOption = {}
dDeprecatedOption["indentSize"] = "option indentSize has been deprecated. Change to indent_size."
dDeprecatedOption["indentStyle"] = "option indentStyle has been deprecated. Change to indent_style."


def check_for_deprecated_rule_options(dConfiguration, sConfigFilename):
    lMessages = []
    lDeprecatedKeys = list(dDeprecatedOption.keys())
    search_dictionary(dConfiguration, lDeprecatedKeys, sConfigFilename, lMessages)

    if len(lMessages) > 0:
        sErrorMessage = ""
        for sMessage in lMessages:
            sErrorMessage += sMessage + "\n"
        raise exceptions.ConfigurationError(sErrorMessage)


def search_dictionary(dDict, lDeprecatedKeys, sConfigFilename, lMessages):
    if len(lDeprecatedKeys) == 0:
        return None
    for sKey in list(dDict.keys()):
        if isinstance(dDict[sKey], dict):
            search_dictionary(dDict[sKey], lDeprecatedKeys, sConfigFilename, lMessages)
        elif isinstance(dDict[sKey], list):
            search_list(dDict[sKey], lDeprecatedKeys, sConfigFilename, lMessages)
        elif sKey in lDeprecatedKeys:
            lMessages.append("ERROR: configuration file " + sConfigFilename + ": " + dDeprecatedOption[sKey])
            lDeprecatedKeys.remove(sKey)


def search_list(lDict, lDeprecatedKeys, sConfigFilename, lMessages):
    if len(lDeprecatedKeys) == 0:
        return None
    for sKey in lDict:
        if isinstance(sKey, dict):
            search_dictionary(sKey, lDeprecatedKeys, sConfigFilename, lMessages)
        elif isinstance(sKey, list):
            search_list(sKey, lDeprectedKeys, sConfigFilename, lMessages)
        elif sKey in lDeprecatedKeys:
            lMessages.append("ERROR: configuration file " + sConfigFilename + ": " + dDeprecatedOption[sKey])
            lDeprecatedKeys.remove(sKey)


def process_file_list_key(dConfig, tempConfiguration, sKey, sConfigFilename):
    dReturn = dConfig
    if "file_list" not in dConfig:
        dReturn["file_list"] = []
    for iIndex, sFilename in enumerate(tempConfiguration["file_list"]):
        validate_file_exists(sFilename, sConfigFilename)
        try:
            for sGlobbedFilename in glob.glob(utils.expand_filename(sFilename), recursive=True):
                dReturn["file_list"].append(sGlobbedFilename)
        except TypeError:
            sKey = list(sFilename.keys())[0]
            for sGlobbedFilename in glob.glob(utils.expand_filename(sKey), recursive=True):
                dTemp = {}
                dTemp[sGlobbedFilename] = {}
                dTemp[sGlobbedFilename].update(tempConfiguration["file_list"][iIndex][sKey])
                dReturn["file_list"].append(dTemp)
    return dReturn


def write_invalid_configuration_junit_file(sFileName, sJUnitFileName):
    if sJUnitFileName:
        oJunitFile = junit.xmlfile(sJUnitFileName)
        oJunitTestsuite = junit.testsuite("vhdl-style-guide", str(0))
        oJunitTestcase = junit.testcase(sFileName, str(0))
        oFailure = junit.failure("Failure")
        oFailure.add_text("Invalid JSON format.  Review configuration for errors.")
        oJunitTestcase.add_failure(oFailure)
        oJunitTestsuite.add_testcase(oJunitTestcase)
        oJunitFile.add_testsuite(oJunitTestsuite)
        utils.write_junit_xml_file(oJunitFile)


def add_debug_to_configuration(oCLA, dConfiguration):
    """
    Adds debug values to the configuration dictionary for later use.

    Parameters:

      oCLA: (command line argument object)

      dConfiguration: (dictionary)

    Returns:  Nothing
    """
    try:
        dConfiguration["debug"] = oCLA.debug
    except TypeError:
        dConfiguration = {}
        dConfiguration["debug"] = oCLA.debug
    return dConfiguration


def read_indent_configuration(dConfiguration):
    """
    Reads the default indent dictionary and merges any changes from a user configuration.

    Parameters:

       dConfiguration: (dictionary)

    Returns:  (dictionary)
    """

    sFileName = os.path.join(os.path.dirname(__file__), "vhdlFile", "indent", "indent_config.yaml")

    dReturn = open_configuration_file(sFileName)

    if "indent" not in list(dConfiguration.keys()):
        dConfiguration["indent"] = dReturn["indent"]
        return dReturn

    ### This merges an indent configuration into the base indent dictionary
    try:
        dGroups = dConfiguration["indent"]["tokens"]
        for sGroup in list(dGroups.keys()):
            for sToken in list(dGroups[sGroup].keys()):
                for sParameter in list(dGroups[sGroup][sToken].keys()):
                    dReturn["indent"]["tokens"][sGroup][sToken][sParameter] = dGroups[sGroup][sToken][sParameter]
    except KeyError:
        report_indent_configuration_error(dReturn, sGroup, sToken)

    dConfiguration["indent"] = dReturn["indent"]

    return dReturn


def report_indent_configuration_error(dReturn, sGroup, sToken):
    print("ERROR: Invalid indent configuration detected")

    report_invalid_indent_group(dReturn, sGroup)
    report_invalid_indent_token(dReturn, sGroup, sToken)


def report_invalid_indent_group(dReturn, sGroup):
    try:
        lTemp = list(dReturn["indent"]["tokens"][sGroup].keys())
    except KeyError:
        print("The following group does not exist")
        print("")
        print("indent:")
        print("    tokens:")
        print(f"        {sGroup}:")
        print("")
        print("The following groups are available:")
        print("")
        print("indent:")
        print("    tokens:")
        for sMyGroup in list(dReturn["indent"]["tokens"].keys()):
            print(f"        {sMyGroup}:")
        sys.exit(1)


def report_invalid_indent_token(dReturn, sGroup, sToken):
    try:
        lTemp = list(dReturn["indent"]["tokens"][sGroup][sToken].keys())
    except KeyError:
        print("The following token does not exist")
        print("")
        print("indent:")
        print("    tokens:")
        print(f"        {sGroup}:")
        print(f"            {sToken}:")
        print("")
        print("The following tokens are available:")
        print("")
        print("indent:")
        print("    tokens:")
        print(f"        {sGroup}:")
        for sMyToken in list(dReturn["indent"]["tokens"][sGroup].keys()):
            print(f"            {sMyToken}:")
        sys.exit(1)


def update_command_line_arguments(commandLineArguments, configuration):
    if "skip_phase" in configuration:
        commandLineArguments.skip_phase = configuration["skip_phase"]
    else:
        commandLineArguments.skip_phase = []

    if not configuration:
        return

    if "file_list" in configuration:
        for sFilename in configuration["file_list"]:
            if isinstance(sFilename, dict):
                sFilename = list(sFilename.keys())[0]
            try:
                lFileNames = glob.glob(utils.expand_filename(sFilename), recursive=True)
                for sFileName in lFileNames:
                    if sFileName not in commandLineArguments.filename:
                        commandLineArguments.filename.append(sFileName)
            except:
                commandLineArguments.filename = glob.glob(utils.expand_filename(sFilename), recursive=True)

    if "local_rules" in configuration:
        commandLineArguments.local_rules = utils.expand_filename(configuration["local_rules"])


dPragmas = {}
dPragmas["open"] = []
dPragmas["close"] = []
dPragmas["single"] = []

dPragmas["open"].append("^\\s*--\\s+synthesis\\s+translate_off\\s*$")
dPragmas["close"].append("^\\s*--\\s+synthesis\\s+translate_on\\s*$")

dPragmas["single"].append("^\\s*--\\s+synthesis\\s+\\w+\\s*$")
dPragmas["single"].append("^\\s*--\\s+synthesis\\s+\\w+\\s+\\w+\\s*$")
dPragmas["single"].append("^\\s*--\\s+pragma\\s+\\w+\\s*$")
dPragmas["single"].append("^\\s*--\\s+pragma\\s+\\w+\\s+\\w+\\s*$")
dPragmas["open"].append("^\\s*--vhdl_comp_off\\s*$")
dPragmas["close"].append("^\\s*--vhdl_comp_on\\s*$")

dPragmas["single"].append("^\\s*--\\s+altera\\s+\\w+\\s*$")

dPragmas["open"].append("^\\s*--\\s+RTL_SYNTHESIS\\s+OFF\\s*$")
dPragmas["close"].append("^\\s*--\\s+RTL_SYNTHESIS\\s+ON\\s*$")

dPragmas["single"].append("^\\s*--\\s+synopsys\\s+\\w+\\s*$")
dPragmas["single"].append("^\\s*--\\s+synopsys\\s+\\w+\\s+\\w+\\s*$")
dPragmas["single"].append("^\\s*--\\s+xilinx\\s+\\w+\\s*$")
dPragmas["single"].append("^\\s*--\\s+xilinx\\s+\\w+\\s+\\w+\\s*$")


def add_pragma_regular_expressions(dStyle):
    if not "pragma" in dStyle.keys():
        dStyle["pragma"] = {}
        dStyle["pragma"]["patterns"] = dPragmas
    dStyle["pragma"]["regexp"] = {}

    try:
        types = list(dStyle["pragma"]["patterns"].keys())
        if "close" not in types:
            dStyle["pragma"]["patterns"]["close"] = []
        if "open" not in types:
            dStyle["pragma"]["patterns"]["open"] = []
        if "single" not in types:
            dStyle["pragma"]["patterns"]["single"] = []

        for types in list(dStyle["pragma"]["patterns"].keys()):
            for pragma in dStyle["pragma"]["patterns"][types]:
                try:
                    dStyle["pragma"]["regexp"][types].append(re.compile(pragma))
                except KeyError:
                    dStyle["pragma"]["regexp"][types] = []
                    dStyle["pragma"]["regexp"][types].append(re.compile(pragma))
    except AttributeError as e:
        print("Error in pragma definition:")
        print('  Refer to "configuring pragmas" section in documentation for details on how to configure pragmas.')
        sys.exit(1)


def New(commandLineArguments):
    oReturn = config()

    dStyle = read_predefined_style(commandLineArguments.style)

    dConfig = read_configuration_files(dStyle, commandLineArguments)

    add_pragma_regular_expressions(dConfig)

    oReturn.severity_list = severity.create_list(dConfig)

    update_command_line_arguments(commandLineArguments, dConfig)

    dConfig = add_debug_to_configuration(commandLineArguments, dConfig)

    oReturn.dConfig = dConfig

    dIndent = read_indent_configuration(dConfig)
    oReturn.dIndent = dIndent

    if commandLineArguments.fix_only:
        oReturn.dFixOnly = open_configuration_file(commandLineArguments.fix_only)
    else:
        oReturn.dFixOnly = None

    return oReturn


class config:
    def __init__(self):
        dIndent = None
        dConfig = None
        dFixOnly = None
        severity_list = None
