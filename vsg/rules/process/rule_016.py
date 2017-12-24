
from vsg import rule


class rule_016(rule.rule):
    '''
    Process rule 016 checks a process has a label.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'process', '016')
        self.solution = 'Add a label for the process.'
        self.phase = 1
        self.fixable = False   # The user must add the label

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessKeyword and not oLine.isProcessLabel:
                self.add_violation(iLineNumber)
