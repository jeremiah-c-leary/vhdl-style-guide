
from vsg import parser
from vsg.rules import move_item_and_items_to_the_right_to_next_line_rule


class rule_010(move_item_and_items_to_the_right_to_next_line_rule):
    '''
    Moves library keyword and code to the right to it's own line.

    '''

    def __init__(self):
        move_item_and_items_to_the_right_to_next_line_rule.__init__(self, 'library', '010', parser.library_keyword)
        self.regionBegin = parser.library_keyword
        self.regionEnd = parser.library_semicolon
