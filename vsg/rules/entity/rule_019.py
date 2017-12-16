
from vsg import rule

import re


class rule_019(rule.rule):
    '''
    Entity rule 019 checks for the entity name on the "end entity" statement.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'entity'
        self.identifier = '019'
        self.solution = 'Add the entity name.'
        self.phase = 1
        self.fixable = False

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndEntityDeclaration and re.match('^\s*end\s+entity', oLine.line, re.IGNORECASE):
                if not re.match('^\s*end\s+entity\s+\w+', oLine.line, re.IGNORECASE):
                    self.add_violation(iLineNumber)
