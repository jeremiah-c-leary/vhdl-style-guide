
from vsg import rule
from vsg import fix

import re


class rule_010(rule.rule):
    '''
    Process rule 010 checks the "generate" keyword is lowercase on the closing of a generate block.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'generate', '010')
        self.solution = 'Lowercase the "generate" keyword.'
        self.phase = 6

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isGenerateEnd and not re.match('^\s*\w+\s+generate', oLine.line):
            self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(oFile.lines[iLineNumber], 'generate')
