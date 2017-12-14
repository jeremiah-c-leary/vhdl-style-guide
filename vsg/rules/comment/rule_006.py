
from vsg import rule
from vsg import check
from vsg import fix
from vsg import line


class rule_006(rule.rule):
    '''
    Comment rule 006 ensures the alignment of "--" keywords between the process sensitivity list and the process "begin" keywords.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'comment'
        self.identifier = '006'
        self.solution = 'Inconsistent alignment of comments process declaration region.'
        self.phase = 6

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSensitivityListEnd and not fGroupFound:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if oLine.isProcessBegin and fGroupFound:
                lGroup.append(oLine)
                fGroupFound = False
                check.keyword_alignment(self, iStartGroupIndex, '--', lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                if oLine.hasComment and not oLine.isComment:
                    lGroup.append(oLine)
                else:
                    lGroup.append(line.line('line removed'))

    def _fix_violations(self, oFile):
        fix.keyword_alignment(self, oFile)
