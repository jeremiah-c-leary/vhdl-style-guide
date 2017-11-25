
from vsg.rules.entity import entity_rule

import re


class rule_015(entity_rule):
    '''
    Entity rule 015 checks the "end" keyword, "entity" keyword, and entity name are on the same line.
    '''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '015'
        self.solution = 'The "end" keyword, "entity" keyword and entity name need to be on the same line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndEntityDeclaration:
                lLine = oLine.line.split()
                if not len(lLine) >= 3:
                    if not (lLine[0] == 'end' and lLine[1] == 'entity' and not lLine[2].startswith('--')):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.line = re.sub(r'^(\s*end)', r'\1 entity', oLine.line, flags=re.IGNORECASE)
            oLine.lineLower = oLine.line.lower()
