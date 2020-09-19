
from vsg.rules import case_item_rule

from vsg.token import context_declaration as token


class rule_015(case_item_rule):
    '''
    Checks the context identifier has proper case.

    '''

    def __init__(self):
        case_item_rule.__init__(self, 'context', '015', token.end_context_keyword)
        self.regionBegin = token.context_keyword
        self.regionEnd = token.semicolon
