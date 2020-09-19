
from vsg.rules import space_between_items_rule

from vsg.token import context_declaration as token


class rule_018(space_between_items_rule):
    '''
    Checks for a single space between the end keyword and the context keyword.

    '''

    def __init__(self):
        space_between_items_rule.__init__(self, 'context', '018', token.end_keyword, token.end_context_keyword)
        self.regionBegin = token.context_keyword
        self.regionEnd = token.semicolon
