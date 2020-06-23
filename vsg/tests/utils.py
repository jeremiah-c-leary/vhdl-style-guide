
import os
import pprint
import yaml


def debug_lines(oFile, iLineNumber, iNumberOfLines):

    for iIndex in range(0, iNumberOfLines):
        print('{0:5d} | {1:s}'.format(iLineNumber + iIndex, oFile.lines[iLineNumber + iIndex].line))


def read_file(sFilename, lLines):
    with open(sFilename) as oFile:
        for sLine in oFile:
            lLines.append(sLine.rstrip())


def print_attributes(oLine):
    pp = pprint.PrettyPrinter(indent = 4)
    pp.pprint(oLine.__dict__)


def remove_file(sFileName):
    try:
        os.remove(sFileName)
    except OSError:
        pass


def read_vhdlfile(sFileName):
    try:
        lLines = []
        with open(sFileName) as oFile:
            for sLine in oFile:
                lLines.append(sLine)
        oFile.close()
        return lLines
    except IOError:
        return []


def add_violation(iLineNumber):
    dViolation = {}
    dViolation['lines'] = []
    dLine = {}
    dLine['number'] = iLineNumber
    dViolation['lines'].append(dLine)
    return dViolation


def add_violation_list(lLineNumbers):
    lReturn = []
    for iLineNumber in lLineNumbers:
        dViolation = {}
        dViolation['lines'] = []
        dLine = {}
        dLine['number'] = iLineNumber
        dViolation['lines'].append(dLine)
        lReturn.append(dViolation)
    return lReturn


def read_configuration(sFileName):
    with open(sFileName) as yaml_file:
        return yaml.full_load(yaml_file)

