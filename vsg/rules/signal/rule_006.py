
from vsg.rules.signal import signal_rule
from vsg import fix

import re


class rule_006(signal_rule):
    '''
    Signal rule 006 checks there is at least a single space before the colon.
    '''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Add a single space before the colon.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                if re.match('^\s*signal\s+.*\S:', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.enforce_one_space_before_word(self, oFile.lines[iLineNumber], ':')
