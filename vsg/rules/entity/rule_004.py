
from vsg.rules.entity import entity_rule


class rule_004(entity_rule):
    '''
    Entity rule 004 checks the entity keyword is lower case.
    '''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change "entity" keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEntityDeclaration:
                self._is_lowercase(oLine.line.split()[0], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'entity')
