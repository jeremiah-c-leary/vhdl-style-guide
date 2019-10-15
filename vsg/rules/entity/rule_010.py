
from vsg.rules import case_rule
from vsg import utils


class rule_010(case_rule):
    '''
    Entity rule 010 checks the "end" keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'entity', '010', 'isEndEntityDeclaration')
        self.solution = 'Change "end" keyword to '

    def _extract(self, oLine):
        return utils.extract_first_keyword(oLine)
