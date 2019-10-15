
from vsg.rules import case_rule
from vsg import utils


class rule_008(case_rule):
    '''
    Entity rule 008 checks the entity name has proper case in the entity declaration line.
    '''

    def __init__(self):
        case_rule.__init__(self, 'entity', '008', 'isEntityDeclaration')
        self.case = 'upper'
        self.solution = 'Change entity name to '

    def _extract(self, oLine):
        return utils.extract_entity_identifier(oLine)
