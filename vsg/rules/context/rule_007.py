
from vsg import parser
from vsg.rules import move_items_after_item_to_next_line_rule


class rule_007(move_items_after_item_to_next_line_rule):
    '''
    Moves code after the is keyword to the next line.

    '''

    def __init__(self):
        move_items_after_item_to_next_line_rule.__init__(self, 'context', '007', parser.context_is_keyword)
        self.solution = 'Move code after the is keyword to the next line'
        self.regionBegin = parser.context_keyword
        self.regionEnd = parser.context_semicolon
