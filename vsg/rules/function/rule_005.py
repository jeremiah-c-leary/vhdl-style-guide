
from vsg.rules.function import function_rule

import re


class rule_005(function_rule):
    '''
    Function rule 005 checks the "function" keyword is lower case.
    '''

    def __init__(self):
        function_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Lowercase the "function" keyword.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isFunctionKeyword:
                if not re.match('^\s*function', oLine.line) and not re.match('^\s*impure\s+function', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'function')
