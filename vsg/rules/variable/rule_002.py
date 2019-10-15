
from vsg.rules import case_rule
from vsg import utils


class rule_002(case_rule):
    '''
    Signal rule 002 checks the "variable" keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'variable', '002', 'isVariable')
        self.solution = 'Change "variable" keyword to '

    def _extract(self, oLine):
        return utils.extract_class_name(oLine)
