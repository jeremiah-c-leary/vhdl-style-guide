
from vsg.rules.generate import generate_rule

import re


class rule_002(generate_rule):
    '''Generate rule 002 checks for a single space between the label and :.'''

    def __init__(self):
        generate_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Ensure a single space exists before the colon.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenerateKeyword:
                if not re.match('^\s*\w+\s:', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_before_word(oFile.lines[iLineNumber], ':')
