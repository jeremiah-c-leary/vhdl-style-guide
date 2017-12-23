
from vsg import rule
from vsg import check
from vsg import fix

import re


class rule_028(rule.rule):
    '''
    Process rule 028 checks the indentation of the closing parenthesis if it is on a line by itself.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'process', '028')
        self.solution = 'Align closing parenthesis with opening parenthesis.'
        self.phase = 5

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSensitivityListBegin and oLine.isSensitivityListEnd:
                continue
            if oLine.insideSensitivityList:
                if oLine.isSensitivityListBegin:
                    iAlignmentColumn = oLine.line.find('(')
                elif oLine.isSensitivityListEnd and re.match('^\s*\)', oLine.line):
                    check.multiline_alignment(self, iAlignmentColumn, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.dFix['violations']:
            fix.multiline_alignment(self, oFile, iLineNumber)
