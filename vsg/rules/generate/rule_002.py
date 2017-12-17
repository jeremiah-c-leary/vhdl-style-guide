
from vsg import rule
from vsg import fix

import re


class rule_002(rule.rule):
    '''Generate rule 002 checks for a single space between the label and :.'''

    def __init__(self):
        rule.rule.__init__(self, 'generate', '002')
        self.solution = 'Ensure a single space exists before the colon.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenerateKeyword and not re.match('^\s*\w+\s:', oLine.line):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.enforce_one_space_before_word(self, oFile.lines[iLineNumber], ':')
