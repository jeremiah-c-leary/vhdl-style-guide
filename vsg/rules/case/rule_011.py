
from vsg.rules.case import case_rule


class rule_011(case_rule):
    '''Case rule 011 ensures the alignment of multiline "when" statements.'''

    def __init__(self):
        case_rule.__init__(self)
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
                self._check_multiline_alignment(iAlignmentColumn, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.dFix['violations']:
            self._fix_multiline_alignment(oFile, iLineNumber)
