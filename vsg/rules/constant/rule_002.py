
from vsg.rules import case_rule
from vsg import utils


class rule_002(case_rule):
    '''
    Constant rule 002 checks the "constant" keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'constant', '002', 'isConstant')
        self.solution = 'Change "constant" keyword to '

    def _extract(self, oLine):
        return utils.extract_class_name(oLine)
