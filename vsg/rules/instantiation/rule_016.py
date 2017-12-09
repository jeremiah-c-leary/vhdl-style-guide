
from vsg import rule
from vsg import fix
from vsg import check


class rule_016(rule.rule):
    '''
    Instantiation rule 016 checks the generic name is uppercase.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '016'
        self.solution = 'Uppercase generic name.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationGenericAssignment and not oLine.isInstantiationGenericKeyword:
                check.is_uppercase(self, oLine.line.split()[0], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            lLine = oFile.lines[iLineNumber].line.split('=>')
            fix.upper_case(self, oFile.lines[iLineNumber], lLine[0].rstrip().lstrip())
