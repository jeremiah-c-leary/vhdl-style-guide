
from vsg.rules.whitespace import whitespace_rule

import re


class rule_001(whitespace_rule):
    '''Whitespace rule 001 checks spaces at the end of lines.'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Remove trailing whitespace.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.line.endswith(' '):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'\s+$', '', oLine.line))
