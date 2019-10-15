
from vsg.rules import case_rule
from vsg import utils


class rule_002(case_rule):
    '''
    Attribute rule 002 checks the **attribute** keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'attribute', '002', 'isAttributeKeyword')
        self.solution = 'Change "attribute" keyword to '

    def _extract(self, oLine):
        return utils.extract_first_keyword(oLine)
