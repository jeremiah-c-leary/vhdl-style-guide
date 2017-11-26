
from vsg.rules.whitespace import whitespace_rule

import re


class rule_003(whitespace_rule):
    '''Whitespace rule 003 checks for spaces before semicolons'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Remove spaces before semicolons.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if ' ;' in oLine.line:
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'(\s+;)', r';', oLine.line))
