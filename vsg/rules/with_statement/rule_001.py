
from vsg import rule


class rule_001(rule.rule):
    '''
    With rule 001 checks for "with" statements.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'with'
        self.identifier = '001'
        self.fixable = False

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isWithKeyword:
                self.add_violation(iLineNumber)
