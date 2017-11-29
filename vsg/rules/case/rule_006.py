
from vsg.rules.case import case_rule
from vsg import fix
from vsg import check
import re


class rule_006(case_rule):
    '''Case rule 006 checks for a single space between the "end" and "case" keywords.'''

    def __init__(self):
        case_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Ensure a single space exists between the "end" and "case" keywords.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndCaseKeyword:
                check.is_single_space_after(self, 'end', oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.enforce_one_space_after_word(self, oFile.lines[iLineNumber], 'end')
