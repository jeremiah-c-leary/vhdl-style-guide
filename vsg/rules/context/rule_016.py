
from vsg.rules import case_item_rule

from vsg.token import context_declaration as token


class rule_016(case_item_rule):
    '''
    Checks the context identifier has proper case.

    '''

    def __init__(self):
        case_item_rule.__init__(self, 'context', '016', token.context_simple_name)
        self.regionBegin = token.context_keyword
        self.regionEnd = token.semicolon
