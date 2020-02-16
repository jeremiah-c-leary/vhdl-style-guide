
from vsg import rule
from vsg import utils

import re


class rule_020(rule.rule):
    '''
    Case rule 020 checks for labels after the "end case" keywords.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'case', '020')
        self.phase = 1
        self.solution = 'Remove label after the "end case" keywords'

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.hasEndCaseLabel:
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = oFile.lines[dViolation['lineNumber']]
            oLine.update_line(re.sub('^(\s*end\s+case)(\s*\w+\s*)(;\s*$)', r'\1\3', oLine.line, 1, flags=re.IGNORECASE))
            oLine.hasEndCaseLabel = False
