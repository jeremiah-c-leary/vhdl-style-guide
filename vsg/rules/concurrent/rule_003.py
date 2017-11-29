
from vsg.rules.concurrent import concurrent_rule
from vsg import check
from vsg import fix


class rule_003(concurrent_rule):
    '''
    Concurrent rule 003 checks the alignment of multiline concurrent assignments.
    '''

    def __init__(self):
        concurrent_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Align first character in row to the column of text one space after the <=.'
        self.phase = 5

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.insideConcurrent:
                if oLine.isConcurrentBegin and oLine.isEndConcurrent:
                    continue
                if oLine.isConcurrentBegin:
                    iAlignmentColumn = oLine.line.find('<') + 3
                else:
                    check.multiline_alignment(self, iAlignmentColumn, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.dFix['violations']:
            fix.multiline_alignment(self, oFile, iLineNumber)
