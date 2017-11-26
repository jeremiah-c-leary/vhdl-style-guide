
from vsg.rules.comment import comment_rule
from vsg import line


class rule_003(comment_rule):
    '''Comment rule 003 ensures the alignment of "--" keywords between process "begin" and "end process" keywords.'''

    def __init__(self):
        comment_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Inconsistent alignment of comments within process.'
        self.phase = 5

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessBegin and not fGroupFound:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if oLine.isEndProcess:
                lGroup.append(oLine)
                fGroupFound = False
                self._check_keyword_alignment(iStartGroupIndex, '--', lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                if oLine.isComment:
                    lGroup.append(line.line('Comment removed'))
                else:
                    lGroup.append(oLine)

    def _fix_violations(self, oFile):
        self._fix_keyword_alignment(oFile)
