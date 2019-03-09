
from vsg import rule


class rule_007(rule.rule):
    '''
    Constant rule 007 checks for assignments in constant declarations.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'constant', '007')
        self.solution = 'move assignment to same line as constant declaration.'
        self.phase = 1
        self.fixable = False  # Too complicated at the moment to fix.

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isConstant and ':=' not in oLine.lineNoComment:
            self.add_violation(iLineNumber)
