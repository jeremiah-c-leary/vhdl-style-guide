
from vsg.rules.entity import entity_rule

import re


class rule_002(entity_rule):
    '''
    Entity rule 002 checks for a single space after the entity keyword.
    '''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Remove extra spaces after entity keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEntityDeclaration:
                if re.match('^\s*\S+\s\s+', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.line = re.sub(r'^(\s*entity)\s+', r'\1 ', oLine.line, flags=re.IGNORECASE)
            oLine.lineLower = oLine.line.lower()
