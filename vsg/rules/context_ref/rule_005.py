
from vsg.rules import move_item_and_items_to_the_right_to_next_line_rule

from vsg.token import context_reference as token


class rule_005(move_item_and_items_to_the_right_to_next_line_rule):
    '''
    Moves context reference keyword, and lines to the right, to the next line.
    '''

    def __init__(self):
        move_item_and_items_to_the_right_to_next_line_rule.__init__(self, 'context_ref', '005', token.keyword)
        self.regionBegin = token.keyword
        self.regionEnd = token.semicolon
