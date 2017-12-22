
from vsg import rule

import re


class rule_001(rule.rule):
    '''Whitespace rule 001 checks spaces at the end of lines.'''

    def __init__(self):
        rule.rule.__init__(self, 'whitespace', '001')
        self.phase = 2
        self.solution = 'Remove trailing whitespace.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.line.endswith(' '):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'\s+$', '', oLine.line))
