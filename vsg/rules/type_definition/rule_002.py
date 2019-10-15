
from vsg.rules import case_rule
from vsg import utils


class rule_002(case_rule):
    '''
    Type rule 002 checks the "type" keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'type', '002', 'isTypeKeyword')
        self.solution = 'Change "type" keyword to '

    def _extract(self, oLine):
        return utils.extract_first_keyword(oLine)
