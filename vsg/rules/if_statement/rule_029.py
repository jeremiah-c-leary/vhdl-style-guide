
from vsg import rule

import re


class rule_029(rule.rule):
    '''
    If rule 029 checks the **then** keyword is lowercase.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'if', '029')
        self.phase = 6
        self.solution = 'lowercase "then" keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isThenKeyword and not oLine.lineNoComment.find('then') > 0:
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub('then', 'then', oLine.line, 1, re.IGNORECASE))
