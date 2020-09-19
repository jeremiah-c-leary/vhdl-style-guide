
from vsg.rules import move_item_next_to_another_item_rule

from vsg.token import context_declaration as token


class rule_005(move_item_next_to_another_item_rule):
    '''
    Checks the "context" identifier is on the same line as the "context" keyword.
    '''

    def __init__(self):
        move_item_next_to_another_item_rule.__init__(self, 'context', '005', token.context_keyword, token.identifier)
        self.subphase = 1
        self.regionBegin = token.context_keyword
        self.regionEnd = token.semicolon
