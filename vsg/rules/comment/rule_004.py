
from vsg import rule
from vsg import fix

import re


class rule_004(rule.rule):
    '''Comment rule 004 ensures there is at least one space before comments on a line with code.'''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'comment'
        self.identifier = '004'
        self.solution = 'Add a space before the comment --'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.hasInlineComment and not re.match('^.*\s--', oLine.line):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.enforce_one_space_before_word(self, oFile.lines[iLineNumber], '--')
