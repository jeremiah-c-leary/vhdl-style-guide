
from vsg import parser
from vsg.rules import move_item_and_items_to_the_right_to_next_line_rule


class rule_011(move_item_and_items_to_the_right_to_next_line_rule):
    '''
    Moves use keyword and code to the right to it's own line.

    '''

    def __init__(self):
        move_item_and_items_to_the_right_to_next_line_rule.__init__(self, 'library', '011', parser.use_keyword)
        self.regionBegin = parser.use_keyword
        self.regionEnd = parser.use_semicolon
