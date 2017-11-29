
from vsg.rules.concurrent import concurrent_rule
from vsg import check
from vsg import fix


class rule_006(concurrent_rule):
    '''
    Concurrent rule 006 ensures the alignment of the "<=" keyword over multiple lines.
    '''

    def __init__(self):
        concurrent_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Inconsistent alignment of "<=" in group of lines.'
        self.phase = 5

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
