
from vsg.rules.case import case_rule
from vsg import check


class rule_008(case_rule):
    '''Case rule 008 ensures a blank line exists below the "case" keyword.'''

    def __init__(self):
        case_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Ensure a blank line exists below the "case" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isCaseIsKeyword:
                check.is_blank_line_after(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._insert_blank_line_below(oFile, iLineNumber)
