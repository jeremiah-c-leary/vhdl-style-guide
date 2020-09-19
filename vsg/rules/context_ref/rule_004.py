
from vsg.rules import case_item_rule

from vsg.token import context_reference as token


class rule_004(case_item_rule):
    '''
    Checks the context selected names have proper case.
    '''
    def __init__(self):
        case_item_rule.__init__(self, 'context_ref', '004', token.selected_name)
        self.regionBegin = token.keyword
        self.regionEnd = token.semicolon
