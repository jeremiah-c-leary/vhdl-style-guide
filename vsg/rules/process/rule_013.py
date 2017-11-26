
from vsg.rules.process import process_rule

import re


class rule_013(process_rule):
    '''
    Process rule 013 checks the "is" keyword is lowercase.
    '''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '013'
        self.solution = 'Lowercase "is" keyword.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSensitivityListEnd:
                if re.match('^.*\)\s*is', oLine.lineLower):
                    if not re.match('^.*\)\s*is', oLine.line):
                      self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'is')
