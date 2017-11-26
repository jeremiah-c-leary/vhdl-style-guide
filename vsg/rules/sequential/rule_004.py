
from vsg.rules.sequential import sequential_rule


class rule_004(sequential_rule):
    '''
    Sequential rule 004 ensures the alignment of multiline sequential statements.
    '''

    def __init__(self):
        sequential_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Align with space after the "<=" keyword.'
        self.phase = 5

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSequential and oLine.isSequentialEnd:
                continue
            if oLine.isSequential:
                iAlignmentColumn = oLine.line.find('<=') + len('<= ')
                continue
            if oLine.insideSequential and not oLine.isComment:
                self._check_multiline_alignment(iAlignmentColumn, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.dFix['violations']:
            self._fix_multiline_alignment(oFile, iLineNumber)
