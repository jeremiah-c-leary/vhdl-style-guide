
from vsg import rule
from vsg import fix

import re


class rule_009(rule.rule):
    '''
    Process rule 009 checks the "process" keyword is lowercase on the closing of a process.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'process', '009')
        self.solution = 'Lowercase the "process" keyword.'
        self.phase = 6

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isEndProcess and not re.match('^\s*\w+\s+process', oLine.line):
            self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(oFile.lines[iLineNumber], 'process')
