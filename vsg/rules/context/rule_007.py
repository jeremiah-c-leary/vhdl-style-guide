
from vsg.rules import move_items_after_item_to_next_line_rule

from vsg.token import context_declaration as token


class rule_007(move_items_after_item_to_next_line_rule):
    '''
    Moves code after the is keyword to the next line.

    '''

    def __init__(self):
        move_items_after_item_to_next_line_rule.__init__(self, 'context', '007', token.is_keyword)
        self.solution = 'Move code after the is keyword to the next line'
        self.regionBegin = token.context_keyword
        self.regionEnd = token.semicolon
