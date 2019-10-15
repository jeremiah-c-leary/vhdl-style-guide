
from vsg.rules import case_rule
from vsg import utils


class rule_026(case_rule):
    '''
    If rule 026 checks the **elsif** keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'if', '026', 'isElseIfKeyword')
        self.solution = 'Change "elsif" keyword to '

    def _extract(self, oLine):
        return utils.extract_first_keyword(oLine)
