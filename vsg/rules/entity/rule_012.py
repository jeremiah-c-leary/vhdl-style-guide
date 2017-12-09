
from vsg import rule
from vsg import fix
from vsg import check

import re


class rule_012(rule.rule):
    '''
    Entity rule 012 checks entity name is uppercase in "end" keyword line.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'entity'
        self.identifier = '012'
        self.solution = 'Uppercase entity name.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndEntityDeclaration and re.match('^\s*end\s+entity\s+\w+', oLine.line, re.IGNORECASE):
                lLine = oLine.line.split()
                check.is_uppercase(self, lLine[2], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.upper_case(self, oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[2])
