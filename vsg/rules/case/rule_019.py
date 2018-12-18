
from vsg import rule

import re


class rule_019(rule.rule):
    '''
    Case rule 019 checks for labels before the case case keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'case', '019')
        self.phase = 1
        self.solution = 'Remove label before "case" keyword'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.hasCaseLabel:
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub('^(\s*)(\w+\s*:\s*)', r'\1', oLine.line, 1))
            oLine.hasCaseLabel = False
