
from vsg.rules import case_item_rule

from vsg.token import entity_declaration as token


class rule_006(case_item_rule):
    '''
    Checks the "is" keyword has proper case.
    '''

    def __init__(self):
        case_item_rule.__init__(self, 'entity', '006', token.is_keyword)
        self.regionBegin = token.is_keyword
        self.regionEnd = token.is_keyword
