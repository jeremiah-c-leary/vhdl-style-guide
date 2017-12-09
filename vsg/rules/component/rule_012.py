
from vsg import rule
from vsg import fix
from vsg import check


class rule_012(rule.rule):
    '''Component rule 012 checks component name is uppercase in "end" keyword line.'''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'component'
        self.identifier = '012'
        self.solution = 'Uppercase component name.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentEnd:
                lLine = oLine.line.split()
                if len(lLine) > 2:
                    check.is_uppercase(self, lLine[2], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            lLine = oFile.lines[iLineNumber].line.split()
            fix.upper_case(self, oFile.lines[iLineNumber], lLine[2])
