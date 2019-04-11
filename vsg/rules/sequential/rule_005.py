
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
        self.lGroup = []
        self.fGroupFound = False
        self.iStartGroupIndex = None

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isSequential and not self.fGroupFound:
            self.fGroupFound = True
            self.iStartGroupIndex = iLineNumber
        if not oLine.insideSequential and self.fGroupFound:
            self.fGroupFound = False
            check.keyword_alignment(self, self.iStartGroupIndex, '<=', self.lGroup)
            self.lGroup = []
            self.iStartGroupIndex = None
        if self.fGroupFound:
            if oLine.isComment:
                self.lGroup.append(line.line('Removed line'))
            else:
                self.lGroup.append(oLine)

    def _fix_violations(self, oFile):
        fix.keyword_alignment(self, oFile)
