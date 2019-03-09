
from vsg import rule


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
            self.add_violation(iLineNumber)
