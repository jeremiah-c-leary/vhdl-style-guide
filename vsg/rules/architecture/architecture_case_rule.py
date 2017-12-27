
from vsg import rule
from vsg import fix
from vsg import check

import re


class architecture_case_rule(rule.rule):
    '''
    Architecture rule 013 checks the architecture name is upper case in the architecture declaration.
    '''

    def __init__(self, name=None, identifier=None, iIndex=None):
        rule.rule.__init__(self, name, identifier)
        self.phase = 6
        self.iIndex = iIndex

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword and re.match('^\s*\S+\s\s*\S+\s\s*of\s\s*\S+\s\s*is', oLine.lineLower):
                lLine = oLine.line.split()
                check.is_uppercase(self, lLine[self.iIndex], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.upper_case(self, oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[self.iIndex])
