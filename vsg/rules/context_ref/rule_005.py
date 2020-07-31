
from vsg import parser
from vsg.rules import move_item_and_items_to_the_right_to_next_line_rule


class rule_005(move_item_and_items_to_the_right_to_next_line_rule):
    '''
    Moves context reference keyword, and lines to the right, to the next line.
    '''

    def __init__(self):
        move_item_and_items_to_the_right_to_next_line_rule.__init__(self, 'context_ref', '005', parser.context_reference_keyword)
        self.regionBegin = parser.context_reference_keyword
        self.regionEnd = parser.context_reference_semicolon
