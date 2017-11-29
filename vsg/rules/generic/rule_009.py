
from vsg.rules.generic import generic_rule
from vsg import fix
from vsg import check


class rule_009(generic_rule):
    '''
    Generic rule 009 checks the "generic" keyword is lowercase.
    '''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Lowercase "generic" keyword.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericKeyword:
                check.is_lowercase(self, oLine.line.split()[0], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(self, oFile.lines[iLineNumber], 'generic')
