
from vsg import rule
from vsg import check
from vsg import fix


class rule_011(rule.rule):
    '''Case rule 011 ensures the alignment of multiline "when" statements.'''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'case'
        self.identifier = '011'
        self.solution = 'Align with space after the "when" keyword.'
        self.phase = 5

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isCaseWhenKeyword and oLine.isCaseWhenEnd:
                continue
            if oLine.isCaseWhenKeyword:
                iAlignmentColumn = (oLine.indentLevel * self.indentSize) + len('when ')
                continue
            if oLine.insideCaseWhen:
                check.multiline_alignment(self, iAlignmentColumn, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.dFix['violations']:
            fix.multiline_alignment(self, oFile, iLineNumber)
