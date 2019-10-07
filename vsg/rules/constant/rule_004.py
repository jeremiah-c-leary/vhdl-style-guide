
from vsg.rules import case_rule
from vsg import utils

class rule_004(case_rule):
    '''
    Constant rule 004 checks the constant names have proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'constant', '004', 'isConstant', utils.extract_class_identifier_list)
        self.solution = 'Change constant identifiers name to ' + self.case + 'case'
