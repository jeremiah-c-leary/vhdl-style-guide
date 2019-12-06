
from vsg.rules import case_rule
from vsg import utils


class rule_010(case_rule):
    '''
    Variable rule 010 checks the variable type has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'variable', '010', 'isVariable')
        self.solution = 'Change variable type name to '

    def _extract(self, oLine):
        return utils.extract_type_name(oLine)
