
from vsg import rule
from vsg import fix
from vsg import utils

import re


class rule_004(rule.rule):
    '''Generate rule 004 checks for a single space between the label and :.'''

    def __init__(self):
        rule.rule.__init__(self, 'for_loop', '004')
        self.solution = 'Ensure a single space exists before the colon.'
        self.phase = 2

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isForLoopLabel and not re.match('^\s*\w+\s:', oLine.line):
            dViolation = utils.create_violation_dict(iLineNumber)
            dViolation['label'] = utils.extract_label(oLine)[0]
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            iLineNumber = dViolation['lineNumber']
            sWord = dViolation['label']
            fix.enforce_one_space_after_word(self, oFile.lines[iLineNumber], sWord)
