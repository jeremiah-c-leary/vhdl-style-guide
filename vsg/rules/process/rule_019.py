
from vsg import rule
from vsg import fix
from vsg import check

import re


class rule_019(rule.rule):
    '''
    Process rule 019 checks the "end process" label is uppercase.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'process', '019')
        self.solution = 'Uppercase the label.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndProcess and re.match('^\s*\w+\s+\w+\s+\w+', oLine.line):
                check.is_uppercase(self, oLine.line.split()[2], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            lLine = oFile.lines[iLineNumber].line.split()
            fix.upper_case(self, oFile.lines[iLineNumber], lLine[2])
