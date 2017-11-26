
from vsg.rules.concurrent import concurrent_rule

import re


class rule_002(concurrent_rule):
    '''
    Concurrent rule 002 checks there is a single space after the assignment.
    '''

    def __init__(self):
        concurrent_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Remove all but one space after the <=.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConcurrentBegin:
                if re.match('^\s*\w+\s*<=\s*[\w|(]', oLine.line):
                    if not re.match('^\s*\w+\s*<=\s[\w|(]', oLine.line):
                        self.add_violation(iLineNumber)
                elif re.match('^\s*\w+\s*:\s*\w+\s*<=\s*[\w|(]', oLine.line):
                    if not re.match('^\s*\w+\s*:\s*\w+\s*<=\s[\w|(]', oLine.line):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], '<=')
