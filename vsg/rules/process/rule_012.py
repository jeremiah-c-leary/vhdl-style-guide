
from vsg import rule

import re


class rule_012(rule.rule):
    '''
    Process rule 012 checks for the existance of the "is" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'process', '012')
        self.solution = 'Add "is" keyword after the closing parenthesis.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSensitivityListEnd and not re.match('^.*\)\s*is', oLine.lineLower):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            iInsertIndex = oLine.line.rfind(')')
            oLine.update_line(oLine.line[:iInsertIndex + 1] + ' is ' + oLine.line[iInsertIndex + 1:])
