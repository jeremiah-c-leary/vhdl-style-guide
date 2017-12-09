
from vsg import rule
from vsg import check
from vsg import fix
from vsg import line


class rule_005(rule.rule):
    '''
    Sequential rule 005 ensures the alignment of the "<=" keyword over
    multiple lines.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'sequential'
        self.identifier = '005'
        self.solution = 'Inconsistent alignment of "<=" in group of lines.'
        self.phase = 5

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSequential and not fGroupFound:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if not oLine.insideSequential and fGroupFound:
                fGroupFound = False
                check.keyword_alignment(self, iStartGroupIndex, '<=', lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                if oLine.isComment:
                    lGroup.append(line.line('Removed line'))
                else:
                    lGroup.append(oLine)

    def _fix_violations(self, oFile):
        fix.keyword_alignment(self, oFile)
