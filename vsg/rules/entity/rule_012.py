
from vsg.rules import case_rule
from vsg import utils


class rule_012(case_rule):
    '''
    Entity rule 012 checks entity name has proper case in the "end" keyword line.
    '''

    def __init__(self):
        case_rule.__init__(self, 'entity', '012', 'isEndEntityDeclaration')
        self.solution = 'Change entity name to '

    def _extract(self, oLine):
        return utils.extract_entity_identifier(oLine)
