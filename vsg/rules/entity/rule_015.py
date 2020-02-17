
from vsg import rule
from vsg import utils

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

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isEndEntityDeclaration:
            if not re.match('^\s*end\s+entity', oLine.line, re.IGNORECASE):
                dViolation = utils.create_violation_dict(iLineNumber)
                self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = oFile.lines[dViolation['lineNumber']]
            oLine.line = re.sub(r'^(\s*end)', r'\1 entity', oLine.line, flags=re.IGNORECASE)
            oLine.lineLower = oLine.line.lower()
