
from vsg import rule
from vsg import check
from vsg import fix


class rule_004(rule.rule):
    '''
    Sequential rule 004 ensures the alignment of multiline sequential
    statements.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'sequential', '004')
        self.solution = 'Align with space after the "<=" keyword.'
        self.phase = 5

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSequential and oLine.isSequentialEnd:
                continue
            if oLine.isSequential:
                iAlignmentColumn = oLine.line.find('<=') + len('<= ')
            if oLine.insideSequential and not oLine.isComment and not oLine.isSequential:
                check.multiline_alignment(self, iAlignmentColumn, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.dFix['violations']:
            fix.multiline_alignment(self, oFile, iLineNumber)
