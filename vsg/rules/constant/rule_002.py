
from vsg.rules import case_rule
from vsg import utils


class rule_002(case_rule):
    '''
    Constant rule 002 checks the "constant" keyword is lowercase.
    '''

    def __init__(self):
        case_rule.__init__(self, 'constant', '002', 'isConstant', utils.extract_class_name)
        self.solution = 'Change constant name to ' + self.case
