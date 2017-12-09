
from vsg import rule

import re


class rule_015(rule.rule):
    '''
    Entity rule 015 checks the "end" keyword, "entity" keyword, and entity name are on the same line.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'entity'
        self.identifier = '015'
        self.solution = 'The "end" keyword, "entity" keyword and entity name need to be on the same line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndEntityDeclaration:
                if not re.match('^\s*end\s+entity', oLine.line, re.IGNORECASE):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.line = re.sub(r'^(\s*end)', r'\1 entity', oLine.line, flags=re.IGNORECASE)
            oLine.lineLower = oLine.line.lower()
