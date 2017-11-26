
from vsg.rules.signal import signal_rule


class rule_008(signal_rule):
    '''
    Signal rule 008 checks for prefixes in signal names.
    '''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Remove default assignment.'
        self.prefixes = None
        self.phase = 7
        self.fixable = False  # The user will have to fix any desired prefixes.

    def analyze(self, oFile):
        if not self.prefixes:
            return
        for iLineNumber, oLine in enumerate(oFile.lines):
            if not oLine.isSignal:
                continue
            for sSignalName in oLine.line.split(':')[0].split():
                if sSignalName.lower() == 'signal':
                    continue
                fPrefixFound = False
                for sPrefixName in self.prefixes:
                    if sSignalName.startswith(sPrefixName):
                        fPrefixFound = True
                        break
                if not fPrefixFound:
                    self.add_violation(iLineNumber)
