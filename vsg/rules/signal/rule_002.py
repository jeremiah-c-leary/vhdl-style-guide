
from vsg import rule
from vsg import utilities
from vsg import fix
from vsg import check


class rule_002(rule.rule):
    '''
    Signal rule 002 checks the "signal" keyword is lowercase.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'signal'
        self.identifier = '002'
        self.solution = 'Lowercase "signal" keyword.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                check.is_lowercase(self, utilities.get_first_word(oLine), iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(self, oFile.lines[iLineNumber], 'signal')
