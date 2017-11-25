
from vsg.rules.entity import entity_rule


class rule_014(entity_rule):
    '''
    Entity rule 014 checks the "entity" keyword is lower case in the closing of the entity.
    '''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '014'
        self.solution = 'Change "entity" keyword to lower case.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndEntityDeclaration:
                lLine = oLine.line.split()
                if len(lLine) >= 3:
                    self._is_lowercase(lLine[1], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'entity')
