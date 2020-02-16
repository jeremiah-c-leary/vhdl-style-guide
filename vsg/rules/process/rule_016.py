
from vsg import rule
from vsg import utils


class rule_016(rule.rule):
    '''
    Process rule 016 checks a process has a label.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'process', '016')
        self.solution = 'Add a label for the process.'
        self.phase = 1
        self.fixable = False   # The user must add the label

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isProcessKeyword and not oLine.isProcessLabel:
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)
