
from vsg.rules import case_rule
from vsg import utils


class rule_025(case_rule):
    '''
    If rule 025 checks the **if** keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'if', '025', 'isIfKeyword')
        self.solution = 'Change "if" keyword to '

    def _extract(self, oLine):
        return utils.extract_first_keyword(oLine)
