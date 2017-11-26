
from vsg.rules.sequential import sequential_rule


class rule_006(sequential_rule):
    '''
    Sequential rule 006 checks for commented out lines within a multiline sequential statement.
    '''

    def __init__(self):
        sequential_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Remove comment.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.insideSequential and oLine.isComment:
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            oFile.lines.pop(iLineNumber)
