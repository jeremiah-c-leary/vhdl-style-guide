
from vsg import rule
from vsg import fix

import re


class rule_006(rule.rule):
    '''Component rule 006 checks the "is" keyword is lower case.'''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'component'
        self.identifier = '006'
        self.solution = 'Change "is" keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentDeclaration and re.match('^\s*\S+\s+\S+\s\s*is', oLine.line, re.IGNORECASE):
                if not re.match('^\s*\S+\s+\S+\s\s*is', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(self, oFile.lines[iLineNumber], 'is')
