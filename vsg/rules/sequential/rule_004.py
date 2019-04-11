
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

    def _pre_analyze(self):
        self.iAlignmentColumn = 0

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isSequential:
            if not oLine.isSequentialEnd:
                self.iAlignmentColumn = oLine.line.find('<=') + len('<= ')
        if oLine.insideSequential and not oLine.isComment and not oLine.isSequential:
            check.multiline_alignment(self, self.iAlignmentColumn, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.dFix['violations']:
            fix.multiline_alignment(self, oFile, iLineNumber)
