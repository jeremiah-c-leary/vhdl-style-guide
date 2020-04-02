
from vsg import rule
from vsg import utils

import re


class rule_011(rule.rule):
    '''
    Generate rule 011 checks the "end generate" has a label.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'generate', '011')
        self.solution = 'Add a label for the "end generate".'
        self.phase = 1

    def _pre_analyze(self):
        self.lGenerateNames = []

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isGenerateLabel:
            self.lGenerateNames.append(utils.extract_label(oLine)[0])
        if oLine.isGenerateEnd and not oLine.isGenerateEndLabel:
            dViolation = utils.create_violation_dict(iLineNumber)
            dViolation['label'] = self.lGenerateNames.pop()
            self.add_violation(dViolation)
        if oLine.isGenerateEnd and oLine.isGenerateEndLabel:
            self.lGenerateNames.pop()

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            iLineNumber = utils.get_violation_line_number(dViolation)
            oLine = oFile.lines[iLineNumber]
            sLine = oLine.line
            iIndex = oLine.lineLower.find('generate') + len('generate')
            oLine.update_line(sLine[:iIndex] + ' ' + dViolation['label'] + sLine[iIndex:])
            oLine.isGenerateEndLabel = True
