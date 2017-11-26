
from vsg.rules.component import component_rule
from vsg import check


class rule_003(component_rule):
    '''
    Component rule 003 checks for a blank line above the component keyword.
    '''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Add blank line above component keyword.'
        self.phase = 3

    def analyze(self, oFile):
        lFailureLines = []
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentDeclaration:
                check.is_blank_line_before(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._insert_blank_line_above(oFile, iLineNumber)
