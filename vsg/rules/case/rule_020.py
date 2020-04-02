
from vsg import rule
from vsg import utils
from vsg import fix

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
            dViolation['label'] = utils.extract_label(oLine)[0]
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = utils.get_violating_line(oFile, dViolation)
            fix.remove_end_label(oLine, dViolation['label'])
            oLine.hasEndCaseLabel = False
