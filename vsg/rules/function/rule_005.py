
from vsg import rule
from vsg import fix

import re


class rule_005(rule.rule):
    '''
    Function rule 005 checks the "function" keyword is lower case.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'function'
        self.identifier = '005'
        self.solution = 'Lowercase the "function" keyword.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isFunctionKeyword and \
               not re.match('^\s*function', oLine.line) and \
               not re.match('^\s*impure\s+function', oLine.line) and \
               not re.match('^\s*pure\s+function', oLine.line):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(self, oFile.lines[iLineNumber], 'function')
