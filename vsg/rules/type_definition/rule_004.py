
from vsg.rules import case_rule
from vsg import utils


class rule_004(case_rule):
    '''
    Type rule 004 checks the type name has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'type', '004', 'isTypeKeyword', utils.extract_type_identifier)
        self.solution = 'Change type identifier name to ' + self.case + 'case'
