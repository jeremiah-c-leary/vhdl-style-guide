
from vsg.rules.case import case_rule
from vsg import check


class rule_007(case_rule):
    '''Case rule 007 ensures a blank line exists before the "case" keyword.'''

    def __init__(self):
        case_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Ensure a blank line exists before the "case" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isCaseKeyword:
                check.is_blank_line_before(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._insert_blank_line_above(oFile, iLineNumber)
