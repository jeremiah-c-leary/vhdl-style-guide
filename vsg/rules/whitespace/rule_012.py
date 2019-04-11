
from vsg import rule


class rule_012(rule.rule):
    '''Whitespace rule 012 checks the number of consecutive blank lines.'''

    def __init__(self):
        rule.rule.__init__(self, 'whitespace', '012')
        self.phase = 3
        self.numBlankLines = 1
        self.solution = 'Remove all but ' + str(self.numBlankLines) + ' blank lines below.'

        self.iNumBlankLines = 0
        self.fFoundFirstBlank = False
        self.iErrorLine = 0

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isBlank and not self.fFoundFirstBlank:
            self.fFoundFirstBlank = True
            self.iErrorLine = iLineNumber
        if oLine.isBlank:
            self.iNumBlankLines += 1
        if self.iNumBlankLines > self.numBlankLines:
            self.add_violation(self.iErrorLine)
            self.dFix['violations'][self.iErrorLine] = self.iNumBlankLines - self.numBlankLines
        if not oLine.isBlank:
            self.fFoundFirstBlank = False
            self.iErrorLine = 0
            self.iNumBlankLines = 0

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            del oFile.lines[iLineNumber:iLineNumber + self.dFix['violations'][iLineNumber]]
