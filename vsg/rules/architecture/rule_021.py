
from vsg import rule
from vsg import fix

import re


class rule_021(rule.rule):
    '''
    Architecture rule 021 checks the "begin" keyword is lower case.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'architecture', '021')
        self.solution = 'Change "begin" keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureBegin and not re.match('^\s*begin', oLine.line):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(self, oFile.lines[iLineNumber], 'begin')
