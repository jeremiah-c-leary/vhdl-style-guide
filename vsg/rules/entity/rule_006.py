
from vsg.rules.entity import entity_rule

import re


class rule_006(entity_rule):
    '''
    Entity rule 006 checks the "is" keyword is lower case.
    '''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Change "is" keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEntityDeclaration:
                lLine = oLine.line.split()
                if len(lLine) > 2:
                    if not re.match('^\s*\S+\s+\S+\s\s*is', oLine.line):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'is')
