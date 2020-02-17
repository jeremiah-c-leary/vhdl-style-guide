
from vsg import rule
from vsg import utils


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
        if not oLine.isBlank:
            if self.iNumBlankLines > self.numBlankLines:
                dViolation = utils.create_violation_dict(self.iErrorLine)
                dViolation['remove'] = self.iNumBlankLines - self.numBlankLines
                self.add_violation(dViolation)
            self.fFoundFirstBlank = False
            self.iErrorLine = 0
            self.iNumBlankLines = 0

    def _fix_violations(self, oFile):
        for dViolation in self.violations[::-1]:
            iLineNumber = dViolation['lineNumber']
            del oFile.lines[iLineNumber:iLineNumber + dViolation['remove']]
