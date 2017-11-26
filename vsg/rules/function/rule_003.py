
from vsg.rules.function import function_rule

import re


class rule_003(function_rule):
    '''
    Function rule 003 checks there is a single space between the function name and the (.
    '''

    def __init__(self):
        function_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Ensure a single space exists between the function name and the (.'
        self.phase = 2

    def analyze(self, oFile):
        fInsideFunction = False
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isFunctionKeyword:
                if not re.match('^\s*function\s+\w+\s\(', oLine.lineLower) and not re.match('^\s*impure\s+function\s+\w+\s\(', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_before_word(oFile.lines[iLineNumber], '\(')
