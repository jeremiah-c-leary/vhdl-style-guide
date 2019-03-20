
from vsg import rule
from vsg import fix
from vsg import check

import re


class uppercase_end_label(rule.rule):
    '''
    Checks for and fixes labels that are lowercase in "end" assignments.
    '''

    def __init__(self, name, identifier, sTrigger):
        rule.rule.__init__(self, name, identifier)
        self.solution = 'Uppercase the label.'
        self.phase = 6
        self.sTrigger = sTrigger

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.__dict__[self.sTrigger] and re.match('^\s*\w+\s+\w+\s+\w+', oLine.line):
            check.is_uppercase(self, oLine.line.split()[2], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            lLine = oFile.lines[iLineNumber].line.split()
            fix.upper_case(self, oFile.lines[iLineNumber], lLine[2])
