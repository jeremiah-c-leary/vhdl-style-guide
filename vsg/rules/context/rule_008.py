
from vsg import parser
from vsg.rules import move_item_and_items_to_the_right_to_next_line_rule


class rule_008(move_item_and_items_to_the_right_to_next_line_rule):
    '''
    Moves code after the is keyword to the next line.

    '''

    def __init__(self):
        move_item_and_items_to_the_right_to_next_line_rule.__init__(self, 'context', '008', parser.context_end_keyword)
        self.regionBegin = parser.context_keyword
        self.regionEnd = parser.context_semicolon
