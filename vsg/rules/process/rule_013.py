
from vsg import rule
from vsg import fix

import re


class rule_013(rule.rule):
    '''
    Process rule 013 checks the "is" keyword is lowercase.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'process', '013')
        self.solution = 'Lowercase "is" keyword.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSensitivityListEnd and re.match('^.*\)\s*is', oLine.lineLower):
                if not re.match('^.*\)\s*is', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(self, oFile.lines[iLineNumber], 'is')
