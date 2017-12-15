
from vsg.rules import keyword_alignment_rule


class rule_006(keyword_alignment_rule):
    '''
    Concurrent rule 006 ensures the alignment of the "<=" keyword over multiple lines.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'concurrent', '006')
        self.solution = 'Inconsistent alignment of "<=" in group of lines.'
        self.

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConcurrentBegin and not fGroupFound:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if not oLine.insideConcurrent and fGroupFound:
                fGroupFound = False
                check.keyword_alignment(self, iStartGroupIndex, '<=', lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                lGroup.append(oLine)

    def _fix_violations(self, oFile):
        fix.keyword_alignment(self, oFile)
