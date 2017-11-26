
from vsg.rules.architecture import architecture_rule


class rule_018(architecture_rule):
    '''Architecture rule 018 checks for a blank line above the "end architecture" keywords.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '018'
        self.solution = 'Add blank line above the "end architecture" keywords.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndArchitecture:
                self._is_blank_line_before(oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._insert_blank_line_above(oFile, iLineNumber)
