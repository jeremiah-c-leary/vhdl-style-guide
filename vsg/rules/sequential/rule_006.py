
from vsg import rule


class rule_006(rule.rule):
    '''
    Sequential rule 006 checks for commented out lines within a multiline sequential statement.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'sequential', '006')
        self.solution = 'Remove comment.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.insideSequential and oLine.isComment:
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            oFile.lines.pop(iLineNumber)
