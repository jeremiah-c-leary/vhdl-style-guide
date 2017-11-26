
from vsg.rules.variable import variable_rule


class rule_007(variable_rule):
    '''
    Signal rule 007 checks for default assignments in variable declarations.
    '''

    def __init__(self):
        variable_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Remove default assignment.'
        self.phase = 1
        self.fixable = False  # Allow the user to decide if these should be removed

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariable:
                if ':=' in oLine.line:
                    self.add_violation(iLineNumber)
