
from vsg.rules.architecture import architecture_rule
from vsg import check


class rule_017(architecture_rule):
    '''Architecture rule 017 checks for a blank line below the "begin" keyword.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '017'
        self.solution = 'Add blank line below the "begin" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureBegin:
                check.is_blank_line_after(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._insert_blank_line_below(oFile, iLineNumber)
