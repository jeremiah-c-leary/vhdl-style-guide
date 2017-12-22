
from vsg import rule
from vsg import fix

import re


class rule_013(rule.rule):
    '''
    Package rule 013 checks the "is" keyword is lower case.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'package'
        self.identifier = '013'
        self.solution = 'Change "is" keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageKeyword and re.match('^\s*package\s+\w+\s+is', oLine.lineLower):
                if not re.match('^\s*\w+\s+\w+\s+is', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(self, oFile.lines[iLineNumber], 'is')
