
from vsg.rules import case_rule
from vsg import utils


class rule_014(case_rule):
    '''
    Entity rule 014 checks the case keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'case', '014', 'isCaseKeyword')
        self.solution = 'Change "case" keyword to '

    def _extract(self, oLine):
        return utils.extract_first_keyword(oLine)
