
from vsg.rules.entity import entity_rule

import re


class rule_007(entity_rule):
    '''
    Entity rule 007 checks for a single space before the "is" keyword.
    '''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Remove extra spaces before "is" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEntityDeclaration:
                if re.match('^.*\s\s+is', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.line = re.sub(r'\s+(is)', r' \1', oLine.line, flags=re.IGNORECASE)
            oLine.lineLower = oLine.line.lower()
