
from vsg.rules import case_rule
from vsg import utils


class rule_027(case_rule):
    '''
    If rule 027 checks the **else** keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'if', '027', 'isElseKeyword')
        self.solution = 'Change "else" keyword to '

    def _extract(self, oLine):
        return utils.extract_first_keyword(oLine)
