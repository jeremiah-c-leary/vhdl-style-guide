import re
import os
import pprint
import yaml

from vsg import config
from vsg import parser
from vsg.vhdlFile import utils as vutils


def debug_lines(oFile, iLineNumber, iNumberOfLines):

    for iIndex in range(0, iNumberOfLines):
        print('{0:5d} | {1:s}'.format(iLineNumber + iIndex, oFile.lines[iLineNumber + iIndex].line))


def read_file(sFilename, lLines, bStrip=True):
    with open(sFilename) as oFile:
        for sLine in oFile:
            if bStrip:
                lLines.append(sLine.rstrip())
            else:
                lLines.append(sLine.strip('\n'))


def print_attributes(oLine):
    pp = pprint.PrettyPrinter(indent = 4)
    pp.pprint(oLine.__dict__)


def remove_file(sFileName):
    try:
        os.remove(sFileName)
    except OSError:
        pass


def read_indent_file():
    sFileName = os.path.join('vsg', 'vhdlFile', 'indent', 'indent_config.yaml')
    with open(sFileName) as yaml_file:
        dFile = yaml.full_load(yaml_file)
    return dFile


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
    oReturn = config.config()
    with open(sFileName) as yaml_file:
        dConfig = yaml.full_load(yaml_file)
    dConfig['debug'] = False
    oReturn.dConfig = dConfig
    return oReturn


def extract_violation_lines(lViolations):
    lReturn = []
    for dViolation in lViolations:
        lReturn.append(dViolation['lines'][0]['number'])
    return lReturn


def extract_violation_lines_from_violation_object(lViolations):
    lReturn = []
    for oViolation in lViolations:
        lReturn.append(oViolation.get_line_number())
    lReturn.sort()
    return lReturn


def validate_token(self, oFile, lExpected, oToken, bDebug=False):
        lActual = []
        for iLine, lLine in enumerate(oFile.get_lines()):
            if bDebug:
                print('-'*80)
                print(lLine.line)
            for iItem, oItem in enumerate(lLine.objects):
                if bDebug:
                    print(oItem)
                if isinstance(oItem, oToken):
                    lActual.append((iLine, iItem))

        self.assertEqual(lExpected, lActual)

def extract_objects(oFile, bIgnoreWhiteSpace=False):
    lReturn = []
    for iLine, oLine in enumerate(oFile.get_object_lines()):
        lReturn.append('-'*80)
        sLine = vutils.convert_token_list_to_string(oLine)
        lReturn.append(f'{iLine} | {sLine}'.rstrip())
        for oObject in oLine:
            if bIgnoreWhiteSpace:
                if type(oObject) == parser.whitespace:
                    continue
            lReturn.append(type(oObject))
    return lReturn

def print_objects(oFile, bIgnoreWhiteSpace=False):
    for line in extract_objects(oFile, bIgnoreWhiteSpace):
        print(line)

def extract_lrm_unit_name(sName):
    return sName.split('.')[-1][5:]


def replace_total_count(lOutput):
    return [re.sub(r'^Total Rules Checked: [1-9][0-9]*$', 'Total Rules Checked: 200', line) for line in lOutput]


def replace_total_count_summary(lOutput):
    return [re.sub(r'\([1-9][0-9]* rules checked\)', '(200 rules checked)', line) for line in lOutput]
