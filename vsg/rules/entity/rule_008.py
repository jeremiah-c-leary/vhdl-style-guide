
from vsg.rules.entity import entity_rule
from vsg import fix
from vsg import check


class rule_008(entity_rule):
    '''
    Entity rule 008 checks the entity name is uppercase in the entity declaration line.
    '''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Change entity name to all uppercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEntityDeclaration:
                check.is_uppercase(self, oLine.line.split()[1], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.upper_case(self, oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[1])
