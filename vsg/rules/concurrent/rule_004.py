
from vsg.rules.concurrent import concurrent_rule

import re


class rule_004(concurrent_rule):
    '''
    Concurrent rule 004 checks there is at least a single space before the assignment.
    '''

    def __init__(self):
        concurrent_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Add a single space before the <=.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConcurrentBegin:
                if re.match('^\s*\w+\s*<=', oLine.line):
                    if not re.match('^\s*\w+\s+<=', oLine.line):
                        self.add_violation(iLineNumber)
                elif re.match('^\s*\w+\s*:\s*\w+\s*<=', oLine.line):
                    if not re.match('^\s*\w+\s*:\s*\w+\s+<=', oLine.line):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(oLine.line.replace('<=',' <='))
