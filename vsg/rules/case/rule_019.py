
from vsg import rule
from vsg import utils
from vsg import fix

import re


class rule_019(rule.rule):
    '''
    Case rule 019 checks for labels before the case case keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'case', '019')
        self.phase = 1
        self.solution = 'Remove label before "case" keyword'

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.hasCaseLabel:
            dViolation = utils.create_violation_dict(iLineNumber)
            dViolation['label'] = utils.extract_label(oLine)[0]
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = oFile.lines[dViolation['lineNumber']]
            fix.remove_begin_label(oLine, dViolation['label'])
            oLine.hasCaseLabel = False
