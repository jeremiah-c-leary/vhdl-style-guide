
from vsg.rules.architecture import architecture_rule
from vsg import check


class rule_016(architecture_rule):
    '''Architecture rule 016 checks for a blank line above the "begin" keyword.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '016'
        self.solution = 'Add blank line above the "begin" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureBegin:
                check.is_blank_line_before(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._insert_blank_line_above(oFile, iLineNumber)
