
from vsg.rules import insert_item_after_item_rule

from vsg.token import context_declaration as token


class rule_021(insert_item_after_item_rule):
    '''
    Checks for the context keyword after the end keyword.

    '''
    def __init__(self):
        insert_item_after_item_rule.__init__(self, 'context', '021', token.end_keyword, token.semicolon, token.end_context_keyword('context'))
        self.insert_space = True
        self.regionBegin = token.context_keyword
        self.regionEnd = token.semicolon
