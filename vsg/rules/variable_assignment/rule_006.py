
from vsg import rule
from vsg import utils


class rule_006(rule.rule):
    '''
    Variable assignment rule 006 checks for commented out lines within a multiline variable_assignment statement.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'variable_assignment', '006')
        self.solution = 'Remove comment.'
        self.phase = 1
        self.fixable = False  # User will have to decide how to handle the comments.

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.insideVariableAssignment and oLine.isComment:
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)
