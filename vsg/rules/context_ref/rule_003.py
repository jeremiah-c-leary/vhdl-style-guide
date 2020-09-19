
from vsg.rules import case_item_rule

from vsg.token import context_reference as token


class rule_003(case_item_rule):
    '''
    Checks the "context" keyword has proper case.
    '''
    def __init__(self):
        case_item_rule.__init__(self, 'context_ref', '003', token.keyword)
        self.regionBegin = token.keyword
        self.regionEnd = token.semicolon
