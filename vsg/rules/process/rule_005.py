
from vsg import rule
from vsg import fix

import re


class rule_005(rule.rule):
    '''
    Process rule 004 checks the "process" keyword is lower case.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'process', '005')
        self.solution = 'Lowercase the "process" keyword.'
        self.phase = 6

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isProcessKeyword and not re.match('^\s*.*process', oLine.line):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(oFile.lines[iLineNumber], 'process')
