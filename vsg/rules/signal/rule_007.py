
from vsg.rules.signal import signal_rule


class rule_007(signal_rule):
    '''
    Signal rule 007 checks for default assignments in signal declarations.
    '''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Remove default assignment.'
        self.phase = 1
        self.fixable = False  # Allow the user to decide if these should be removed

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                if ':=' in oLine.line:
                    self.add_violation(iLineNumber)
