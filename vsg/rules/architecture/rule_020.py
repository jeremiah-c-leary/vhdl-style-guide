
from vsg import rule
from vsg import fix

import re


class rule_020(rule.rule):
    '''
    Architecture rule 020 checks the "is" keyword is lower case.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'architecture', '020')
        self.solution = 'Change "is" keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword:
                if re.match('^\s*architecture\s+\w+\s+of\s+\w+\s+is', oLine.lineLower):
                    if not re.match('^\s*\w+\s+\w+\s+\w+\s+\w+\s+is', oLine.line):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(self, oFile.lines[iLineNumber], 'is')
