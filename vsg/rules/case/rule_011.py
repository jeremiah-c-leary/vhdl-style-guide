
from vsg import rule
from vsg import check
from vsg import fix


class rule_011(rule.rule):
    '''
    Case rule 011 ensures the alignment of multiline "when" statements.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'case'
        self.identifier = '011'
        self.solution = 'Align with space after the "when" keyword.'
        self.phase = 5
        # Variables required for analysis
        self.iAlignmentColumn = 0

    def _pre_analyze(self):
        self.iAlignmentColumn = 0

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isCaseWhenKeyword:
            if not oLine.isCaseWhenEnd:
                self.iAlignmentColumn = (oLine.indentLevel * self.indentSize) + len('when ')
        elif oLine.insideCaseWhen:
            check.multiline_alignment(self, self.iAlignmentColumn, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.dFix['violations']:
            fix.multiline_alignment(self, oFile, iLineNumber)
