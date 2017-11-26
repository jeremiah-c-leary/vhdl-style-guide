
from vsg.rules.architecture import architecture_rule
from vsg import check


class rule_015(architecture_rule):
    '''Architecture rule 015 checks for a blank line below the architecture keyword.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '015'
        self.solution = 'Add blank line below architecture keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword:
                check.is_blank_line_after(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._insert_blank_line_below(oFile, iLineNumber)
