
from vsg import rule
from vsg import check
from vsg import fix

import re


class rule_020(rule.rule):
    '''
    Process rule 020 checks the indentation on multiline sensitivity lists.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'process', '020')
        self.solution = 'Fix indentation of sensitivity list.'
        self.phase = 5

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSensitivityListBegin and oLine.isSensitivityListEnd:
                continue
            if oLine.insideSensitivityList:
                if oLine.isSensitivityListBegin:
                    iAlignmentColumn = oLine.line.find('(')
                elif oLine.isSensitivityListEnd and re.match('^\s*\)', oLine.line):
                    continue
                else:
                    check.multiline_alignment(self, iAlignmentColumn + 1, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.dFix['violations']:
            fix.multiline_alignment(self, oFile, iLineNumber)
