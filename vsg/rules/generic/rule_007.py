
from vsg import rule
from vsg import fix
from vsg import check


class rule_007(rule.rule):
    '''
    Generic rule 007 checks generic names are uppercase.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'generic'
        self.identifier = '007'
        self.solution = 'Uppercase generic name.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericDeclaration and not oLine.isGenericKeyword:
                check.is_uppercase(self, oLine.line.split()[0], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.upper_case(self, oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[0])
