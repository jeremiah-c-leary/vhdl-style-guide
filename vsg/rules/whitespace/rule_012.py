
from vsg import rule


class rule_012(rule.rule):
    '''Whitespace rule 012 checks the number of consecutive blank lines.'''

    def __init__(self):
        rule.rule.__init__(self, 'whitespace', '012')
        self.phase = 3
        self.numBlankLines = 1
        self.solution = 'Remove all but ' + str(self.numBlankLines) + ' blank lines below.'

    def analyze(self, oFile):
        iNumBlankLines = 0
        fFoundFirstBlank = False
        iErrorLine = 0
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isBlank and not fFoundFirstBlank:
                fFoundFirstBlank = True
                iErrorLine = iLineNumber
            if oLine.isBlank:
                iNumBlankLines += 1
            if iNumBlankLines > self.numBlankLines:
                self.add_violation(iErrorLine)
                self.dFix['violations'][iErrorLine] = iNumBlankLines - self.numBlankLines
            if not oLine.isBlank:
                fFoundFirstBlank = False
                iErrorLine = 0
                iNumBlankLines = 0

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            for iIndex in range (0, self.dFix['violations'][iLineNumber]):
                oFile.lines.pop(iLineNumber)
