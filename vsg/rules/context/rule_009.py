
from vsg.rules import move_item_next_to_another_item_rule

from vsg.token import context_declaration as token


class rule_009(move_item_next_to_another_item_rule):
    '''
    Checks the context keyword is on the same line as the end context keyword.

    '''

    def __init__(self):
        move_item_next_to_another_item_rule.__init__(self, 'context', '009', token.end_keyword, token.end_context_keyword)
        self.solution = None
        self.subphase = 1
        self.regionBegin = token.context_keyword
        self.regionEnd = token.semicolon
