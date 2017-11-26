
from vsg.rules.instantiation import instantiation_rule
from vsg import check


class rule_004(instantiation_rule):
    '''
    Instantiation rule 004 checks for a blank line above the instantiation declaration.
    '''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Add blank line above instantiation declaration.'
        self.phase = 3

    def analyze(self, oFile):
        lFailureLines = []
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationDeclaration:
                check.is_blank_line_before(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._insert_blank_line_above(oFile, iLineNumber)
