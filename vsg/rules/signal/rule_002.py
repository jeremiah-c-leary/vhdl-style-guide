
from vsg.rules.signal import signal_rule


class rule_002(signal_rule):
    '''
    Signal rule 002 checks the "signal" keyword is lowercase.
    '''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Lowercase "signal" keyword.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                self._is_lowercase(self._get_first_word(oLine), iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'signal')
