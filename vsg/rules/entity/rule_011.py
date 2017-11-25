
from vsg.rules.entity import entity_rule

import re

class rule_011(entity_rule):
    '''
    Entity rule 011 checks for a single space after the "end" keyword
    '''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '011'
        self.solution = 'Reduce spaces after "end" keyword to one.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndEntityDeclaration:
                if re.match('^\s*\S+\s\s+\S', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.line = re.sub(r'^(\s*end)\s+', r'\1 ', oLine.line, flags=re.IGNORECASE)
            oLine.lineLower = oLine.line.lower()
