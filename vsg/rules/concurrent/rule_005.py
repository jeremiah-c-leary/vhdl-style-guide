
from vsg import rule
from vsg import utils
from vsg import fix

import re


class rule_005(rule.rule):
    '''
    Concurrent rule 005 checks for labels on concurrent assignments.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'concurrent'
        self.identifier = '005'
        self.solution = 'Remove label on concurrent assignment.'
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.hasConcurrentLabel:
            dViolation = utils.create_violation_dict(iLineNumber)
            dViolation['label'] = utils.extract_label(oLine)[0]
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = utils.get_violating_line(oFile, dViolation)
            fix.remove_begin_label(oLine, dViolation['label'])
            oLine.hasConcurrentLabel = False
