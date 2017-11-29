
from vsg.rules.case import case_rule
from vsg import fix
from vsg import check
import re


class rule_002(case_rule):
    '''Case rule 002 checks for a single space after the "case" keyword.'''

    def __init__(self):
        case_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Ensure a single space exists after the "case" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isCaseKeyword:
                check.is_single_space_after(self, 'case', oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.enforce_one_space_after_word(self, oFile.lines[iLineNumber], 'case')
