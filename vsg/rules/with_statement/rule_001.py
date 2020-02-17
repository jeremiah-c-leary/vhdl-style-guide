
from vsg import rule
from vsg import utils


class rule_001(rule.rule):
    '''
    With rule 001 checks for "with" statements.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'with', '001')
        self.fixable = False
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isWithKeyword:
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)
