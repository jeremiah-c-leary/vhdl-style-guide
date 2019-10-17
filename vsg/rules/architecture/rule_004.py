
from vsg import rule
from vsg import fix

import re


class rule_004(rule.rule):
    '''
    Architecture rule 004 checks the architecture keyword is lower case.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'architecture', '004')
        self.solution = 'Change architecture keyword to lowercase.'
        self.phase = 6

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isArchitectureKeyword and not re.match('^\s*architecture', oLine.line):
            self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(oFile.lines[iLineNumber], 'architecture')
