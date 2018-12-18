
from vsg import rule

import re


class rule_020(rule.rule):
    '''
    Case rule 020 checks for labels after the "end case" keywords.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'case', '020')
        self.phase = 1
        self.solution = 'Remove label after the "end case" keywords'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.hasEndCaseLabel:
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub('^(\s*end\s+case)(\s*\w+\s*)(;\s*$)', r'\1\3', oLine.line, 1, flags=re.IGNORECASE))
            oLine.hasEndCaseLabel = False
