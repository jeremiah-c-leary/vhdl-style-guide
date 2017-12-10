
from vsg import rule
from vsg import fix
from vsg import check

import re


class rule_014(rule.rule):
    '''
    Entity rule 014 checks the "entity" keyword is lower case in the closing of the entity.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'entity'
        self.identifier = '014'
        self.solution = 'Change "entity" keyword to lower case.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndEntityDeclaration and re.match('^\s*end\s+entity', oLine.line, re.IGNORECASE):
                lLine = oLine.line.split()
                check.is_lowercase(self, lLine[1], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(self, oFile.lines[iLineNumber], 'entity')
