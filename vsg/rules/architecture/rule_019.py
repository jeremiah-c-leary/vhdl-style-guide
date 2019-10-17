
from vsg import rule
from vsg import fix

import re


class rule_019(rule.rule):
    '''
    Architecture rule 019 checks the "of" keyword is lower case.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'architecture', '019')
        self.solution = 'Change "of" keyword to lowercase.'
        self.phase = 6

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isArchitectureKeyword and \
           re.match('^\s*\w+\s+\w+\s+of', oLine.lineLower) and \
           not re.match('^\s*\w+\s+\w+\s+of', oLine.line):
            self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(oFile.lines[iLineNumber], 'of')
