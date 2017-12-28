
from vsg import rule


class rule_008(rule.rule):
    '''
    Signal rule 008 checks for prefixes in signal names.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'signal', '008')
        self.solution = 'Invalid or missing prefix.'
        self.prefixes = None
        self.phase = 7
        self.fixable = False  # The user will have to fix any desired prefixes.

    def analyze(self, oFile):
        if not self.prefixes:
            return
        for iLineNumber, oLine in enumerate(oFile.lines):
            if not oLine.isSignal:
                continue
            check_for_signal_prefixes(self, oLine, iLineNumber)


def check_for_signal_prefixes(self, oLine, iLineNumber):
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
