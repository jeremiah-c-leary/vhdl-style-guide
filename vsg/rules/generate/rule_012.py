
from vsg import rule
from vsg import fix
from vsg import check

import re


class rule_012(rule.rule):
    '''
    Generate rule 012 checks the "end generate" label is uppercase.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'generate', '012')
        self.solution = 'Uppercase the label.'
        self.phase = 6

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isGenerateEnd and re.match('^\s*\w+\s+\w+\s+\w+', oLine.line):
            check.is_uppercase(self, oLine.line.split()[2], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            lLine = oFile.lines[iLineNumber].line.split()
            fix.upper_case(self, oFile.lines[iLineNumber], lLine[2])
