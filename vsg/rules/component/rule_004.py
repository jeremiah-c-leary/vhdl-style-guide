
from vsg.rules import case_rule
from vsg import utils

class rule_004(case_rule):
    '''
    Component rule 004 checks the component keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'component', '004', 'isComponentDeclaration', utils.extract_first_word)
        self.solution = 'Change component keyword to ' + self.case + 'case'
