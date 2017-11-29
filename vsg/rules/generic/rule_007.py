
from vsg.rules.generic import generic_rule
from vsg import fix
from vsg import check


class rule_007(generic_rule):
    '''
    Generic rule 007 checks generic names are uppercase.
    '''

    def __init__(self):
        generic_rule.__init__(self)
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
