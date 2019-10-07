
from vsg.rules import case_rule
from vsg import utils


class rule_025(case_rule):
    '''
    If rule 025 checks the **if** keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'if', '025', 'isIfKeyword', utils.extract_first_keyword)
        self.solution = 'Change if keyword to ' + self.case + 'case'
