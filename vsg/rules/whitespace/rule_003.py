
from vsg import rule

import re


class rule_003(rule.rule):
    '''Whitespace rule 003 checks for spaces before semicolons'''

    def __init__(self):
        rule.rule.__init__(self, 'whitespace', '003')
        self.phase = 2
        self.solution = 'Remove spaces before semicolons.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if ' ;' in oLine.line:
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'(\s+;)', r';', oLine.line))
