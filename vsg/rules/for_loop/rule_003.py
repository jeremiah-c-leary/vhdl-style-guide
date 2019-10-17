
from vsg import rule
from vsg import fix


class rule_003(rule.rule):
    '''Generate rule 003 checks the for loop label is uppercase.'''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'for_loop'
        self.identifier = '003'
        self.solution = 'Uppercase for loop label.'
        self.phase = 6

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isForLoopLabel:
            lLine = oLine.line.split(':')
            if not lLine[0] == lLine[0].upper():
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.upper_case(oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split(':')[0].lstrip().rstrip())
