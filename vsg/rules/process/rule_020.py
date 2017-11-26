
from vsg.rules.process import process_rule

import re


class rule_020(process_rule):
    '''
    Process rule 020 checks the indentation on multiline sensitivity lists.
    '''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '020'
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
                    self._check_multiline_alignment(iAlignmentColumn, oLine, iLineNumber)
                else:
                    self._check_multiline_alignment(iAlignmentColumn + 1, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.dFix['violations']:
            self._fix_multiline_alignment(oFile, iLineNumber)
