
from vsg.rules.constant import constant_rule


class rule_007(constant_rule):
    '''
    Constant rule 007 checks for assignments in constant declarations.
    '''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'move assignment to same line as constant declaration.'
        self.phase = 1
        self.fixable = False  # Too complicated at the moment to fix.

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConstant:
                if ':=' not in oLine.line:
                    self.add_violation(iLineNumber)
