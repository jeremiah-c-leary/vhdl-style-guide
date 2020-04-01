
from vsg import rule
from vsg import utils

import re


class rule_019(rule.rule):
    '''
    Component rule 019 checks for comments after port and generic assignments.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'component'
        self.identifier = '019'
        self.solution = 'Remove comment.'
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.insideComponent and oLine.hasInlineComment:
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = utils.get_violating_line(oFile, dViolation)
            oLine.update_line(re.sub('\s*--.*', '', oLine.line))
            oLine.hasInlineComment = False
