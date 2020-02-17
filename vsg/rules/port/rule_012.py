
from vsg import rule
from vsg import utils


class rule_012(rule.rule):
    '''
    Port rule 012 checks for default assignments in port declarations.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'port', '012')
        self.solution = 'Remove default assignment in port declaration'
        self.phase = 1
        self.fixable = False  # Allow user to fix the default assignments

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isPortDeclaration and ':=' in oLine.line:
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)
