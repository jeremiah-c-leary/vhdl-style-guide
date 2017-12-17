
from vsg import rule


class rule_007(rule.rule):
    '''
    Signal rule 007 checks for default assignments in variable declarations.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'variable', '007')
        self.solution = 'Remove default assignment.'
        self.phase = 1
        self.fixable = False  # Allow the user to decide if these should be removed

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariable and ':=' in oLine.line:
                self.add_violation(iLineNumber)
