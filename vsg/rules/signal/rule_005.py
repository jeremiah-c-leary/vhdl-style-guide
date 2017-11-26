
from vsg.rules.signal import signal_rule

import re


class rule_005(signal_rule):
    '''
    Signal rule 005 checks there is a single space after the colon.
    '''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Ensure only a signal space after the colon.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                if not re.match('^\s*signal\s+.*\s*:\s\S', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], ':')
