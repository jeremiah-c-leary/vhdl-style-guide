
from vsg.rules import case_rule
from vsg import utils


class rule_011(case_rule):
    '''
    Constant rule 011 checks the constant type has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'constant', '011', 'isConstant')
        self.solution = 'Change type name to '

    def _extract(self, oLine):
        return utils.extract_type_name(oLine)
