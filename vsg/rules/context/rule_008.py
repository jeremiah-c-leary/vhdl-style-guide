
from vsg.rules import move_item_and_items_to_the_right_to_next_line_rule

from vsg.token import context_declaration as token


class rule_008(move_item_and_items_to_the_right_to_next_line_rule):
    '''
    Moves code after the is keyword to the next line.

    '''

    def __init__(self):
        move_item_and_items_to_the_right_to_next_line_rule.__init__(self, 'context', '008', token.end_keyword)
        self.regionBegin = token.context_keyword
        self.regionEnd = token.semicolon
