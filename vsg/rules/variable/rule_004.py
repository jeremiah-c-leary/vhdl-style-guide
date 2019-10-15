
from vsg.rules import case_rule
from vsg import utils


class rule_004(case_rule):
    '''
    Variable rule 004 checks the variable identifiers have proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'variable', '004', 'isVariable')
        self.solution = 'Change variable identifiers name to '

    def _extract(self, oLine):
        return utils.extract_class_identifier_list(oLine)
