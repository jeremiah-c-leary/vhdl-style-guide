
from vsg.rules.instantiation import instantiation_rule
from vsg import check


class rule_019(instantiation_rule):
    '''
    Instantiation rule 019 checks for a blank line below the end of the port declaration.
    '''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '019'
        self.solution = 'Add blank line below instantiation declaration.'
        self.phase = 3

    def analyze(self, oFile):
        lFailureLines = []
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationPortEnd:
                check.is_blank_line_after(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._insert_blank_line_below(oFile, iLineNumber)
