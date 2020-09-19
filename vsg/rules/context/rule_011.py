
from vsg.rules import move_item_next_to_one_of_several_items_rule

from vsg.token import context_declaration as token


class rule_011(move_item_next_to_one_of_several_items_rule):
    '''
    Checks the context keyword is on the same line as the end context keyword.

    '''
    def __init__(self):
        move_item_next_to_one_of_several_items_rule.__init__(self, 'context', '011', [token.context_simple_name, token.end_context_keyword, token.end_keyword], token.semicolon)
        self.solution = None
        self.subphase = 3
        self.regionBegin = token.context_keyword
        self.regionEnd = token.semicolon
