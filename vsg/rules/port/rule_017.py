
from vsg.rules import case_rule
from vsg import utils

class rule_017(case_rule):
    '''
    Port rule 017 checks the "port" keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'port', '017', 'isPortKeyword', utils.extract_first_keyword)
        self.solution = 'Change port keyword to ' + self.case + 'case'
