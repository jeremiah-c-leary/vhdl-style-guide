
from vsg.token import use_clause
from vsg.rules import move_item_and_items_to_the_right_to_next_line_rule


class rule_011(move_item_and_items_to_the_right_to_next_line_rule):
    '''
    Moves use keyword and code to the right to it's own line.

    '''

    def __init__(self):
        move_item_and_items_to_the_right_to_next_line_rule.__init__(self, 'library', '011', use_clause.keyword)
        self.regionBegin = use_clause.keyword
        self.regionEnd = use_clause.semicolon
