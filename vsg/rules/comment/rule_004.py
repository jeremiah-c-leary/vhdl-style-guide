
from vsg.rules.comment import comment_rule

import re

class rule_004(comment_rule):
    '''Comment rule 004 ensures there is at least one space before comments on a line with code.'''

    def __init__(self):
        comment_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Add a space before the comment --'
        self.phase = 2

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.hasComment and not oLine.isComment:
                if not re.match('^.*\s--', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_before_word(oFile.lines[iLineNumber], '--')
