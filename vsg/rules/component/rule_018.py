
from vsg.rules.component import component_rule


class rule_018(component_rule):
    '''
    Component rule 018 checks for a blank line below the
    "end component" keywords.
    '''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '018'
        self.solution = 'Add blank line after "end component" keywords.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentEnd:
                self._is_blank_line_after(oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._insert_blank_line_below(oFile, iLineNumber)
