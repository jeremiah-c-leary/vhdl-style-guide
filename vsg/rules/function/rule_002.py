
from vsg.rules.function import function_rule

import re


class rule_002(function_rule):
    '''
    Function rule 002 checks there is a single space between the function keyword and the function name.
    '''

    def __init__(self):
        function_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Ensure a single space exists between the "function" keyword and the function name.'
        self.phase = 2

    def analyze(self, oFile):
        fInsideFunction = False
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isFunctionKeyword:
                if not re.match('^\s*function\s\w', oLine.lineLower) and not re.match('^\s*impure\s+function\s\w', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], 'function')
