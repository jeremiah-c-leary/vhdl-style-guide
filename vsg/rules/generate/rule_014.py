
from vsg import rule
from vsg import fix
from vsg import utils

import re


class rule_014(rule.rule):
    '''Generate rule 014 checks for a single space between the label and :.'''

    def __init__(self):
        rule.rule.__init__(self, 'generate', '014')
        self.solution = 'Ensure a single space exists before the colon.'
        self.phase = 2

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isGenerateKeyword and oLine.isGenerateLabel and not re.match('^\s*\w+\s*:\s\w+', oLine.line):
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            fix.enforce_one_space_after_word(self, oFile.lines[dViolation['lineNumber']], ':')
