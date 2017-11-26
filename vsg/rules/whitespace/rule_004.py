
from vsg.rules.whitespace import whitespace_rule

import re


class rule_004(whitespace_rule):
    '''Whitespace rule 004 checks for spaces before commas.'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Remove spaces before commas.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if ' ,' in oLine.line:
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'(\s+,)', r',', oLine.line))
