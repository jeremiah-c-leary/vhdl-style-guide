# -*- coding: utf-8 -*-
import argparse
import os
import sys

from . import config, rule_list, vhdlFile


def parse_command_line_arguments():
    """Parses the command line arguments and returns them."""

    parser = argparse.ArgumentParser(prog="VHDL Style Guide (VSG) Rule Documentation Generator", description="""Outputs formatted rule documentation.""")

    sDocsPath = os.path.join(os.path.dirname(__file__), "../docs")

    parser.add_argument("-p", "--path", default=sDocsPath, help="Path in which to generate the rule documentation")

    return parser.parse_args()


def main():
    """Main routine of parser output"""

    fExitStatus = 0

    commandLineArguments = parse_command_line_arguments()

    create_rule_documentation(commandLineArguments.path)

    sys.exit(fExitStatus)


def create_rule_documentation(path):
    oRuleList = build_rule_list()

    dRules = build_rule_dictionary(oRuleList)
    lRuleNames = get_names_of_rule_classes(oRuleList)
    for sRuleName in lRuleNames:
        build_rule_class_doc(path, sRuleName, dRules)


def build_rule_class_doc(path, sRuleName, dRules):
    lRuleClassDoc = []
    lRuleClassDoc.append(".. include:: includes.rst")
    lRuleClassDoc.extend(blank_line())
    if sRuleName == "context_ref":
        sTitle = "Context Reference Rules"
    elif sRuleName == "exit_statement":
        sTitle = "Exit Rules"
    else:
        sTitle = (sRuleName.title() + " Rules").replace("_", " ")
    lRuleClassDoc.append(sTitle)
    lRuleClassDoc.append("-" * len(sTitle))
    lRuleClassDoc.extend(blank_line())
    lRuleClassDoc.extend(import_preamble_doc(sRuleName))
    lRuleClassDoc.extend(do_something(list(dRules[sRuleName])))

    write_file(path, f"{sRuleName}_rules.rst", lRuleClassDoc)


def import_preamble_doc(sRuleName):
    lReturn = []
    if sRuleName == "range":
        sFileName = f"vsg/rules/ranges/preamble_doc.rst"
    else:
        sFileName = f"vsg/rules/{sRuleName}/preamble_doc.rst"
    if os.path.exists(sFileName):
        lReturn = read_file(sFileName)
        lReturn.extend(blank_line())
    return lReturn


def build_rule_list():
    oVhdlFile = vhdlFile.vhdlFile([""])
    oConfig = config.config()
    return rule_list.rule_list(oVhdlFile, oConfig)


def build_rule_dictionary(oRuleList):
    lRuleName = []
    dRules = {}
    for oRule in oRuleList.rules:
        if oRule.name not in lRuleName:
            lRuleName.append(oRule.name)
            dRules[oRule.name] = []
        dRules[oRule.name].append(oRule)

    return dRules


def get_names_of_rule_classes(oRuleList):
    lRuleName = []
    for oRule in oRuleList.rules:
        if oRule.name not in lRuleName:
            lRuleName.append(oRule.name)
    return lRuleName


def do_something(lRules):
    lRuleDoc = []
    for oRule in lRules:
        lRuleDoc.extend(generate_rule_header(oRule))
        lRuleDoc.extend(blank_line())
        if not oRule.deprecated and not oRule.proposed:
            lRuleDoc.extend(generate_icons(oRule))
            lRuleDoc.extend(blank_line())
        lRuleDoc.extend(add_doc_string(oRule))
    return lRuleDoc


def add_doc_string(oRule):
    lReturn = []
    sReturn = oRule.__doc__
    iFirstCharacter = find_index_of_first_character(sReturn)
    sReturn = sReturn[iFirstCharacter:]
    sReturn = sReturn.replace("\n" + " " * (iFirstCharacter - 1), "\n")
    sReturn = sReturn.replace("\n" + " " * (iFirstCharacter - 2) + "\n", "\n\n")
    sReturn = sReturn.replace("[Violation]", "**Violation**\n\n.. code-block:: vhdl")
    sReturn = sReturn.replace("[Fix]", "**Fix**\n\n.. code-block:: vhdl")
    lReturn.append(sReturn)
    return lReturn


def find_index_of_first_character(sReturn):
    for iChar, sChar in enumerate(sReturn):
        if sChar != " " and sChar != "\n":
            return iChar
    return None


def generate_rule_header(oRule):
    lReturn = []
    lReturn.append(oRule.unique_id)
    lReturn.append("#" * len(oRule.unique_id))
    return lReturn


def blank_line():
    lReturn = []
    lReturn.append("")
    return lReturn


def write_file(path, sFilename, lLines):
    with open(os.path.join(path, sFilename), "w") as oFile:
        oFile.write("\n".join(lLines))


def read_file(sFileName):
    lLines = []
    with open(sFileName) as oFile:
        for sLine in oFile:
            lLines.append(sLine.rstrip())
    return lLines


def generate_icons(oRule):
    sIcons = ""
    sIcons += create_phase_icon(oRule)
    sIcons += create_disabled_icon(oRule)
    sIcons += create_severity_icon(oRule)
    sIcons += create_unfixable_icon(oRule)
    sIcons += create_group_icons(oRule)
    return [sIcons]


def create_phase_icon(oRule):
    return "|phase_" + str(oRule.phase) + "|"


def create_disabled_icon(oRule):
    sReturn = ""
    if oRule.disable:
        sReturn += " "
        sReturn += "|disabled|"
    return sReturn


def create_severity_icon(oRule):
    sReturn = " "
    sReturn += "|" + oRule.severity.name.lower() + "|"
    return sReturn


def create_unfixable_icon(oRule):
    sReturn = ""
    if not oRule.fixable:
        sReturn += " "
        sReturn += "|unfixable|"
    return sReturn


def create_group_icons(oRule):
    sReturn = ""
    for sGroup in oRule.groups:
        sReturn += " "
        sReturn += "|" + sGroup.replace("::", "_") + "|"
    return sReturn


if __name__ == "__rule_doc_gen__":
    main()
