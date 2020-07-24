
from vsg import parser
from vsg.rules import move_item_next_to_one_of_several_items_rule


class rule_011(move_item_next_to_one_of_several_items_rule):
    '''
    Checks the context keyword is on the same line as the end context keyword.

    '''

    def __init__(self):
        move_item_next_to_one_of_several_items_rule.__init__(self, 'context', '011', [parser.context_end_identifier, parser.context_end_context_keyword, parser.context_end_keyword], parser.context_semicolon)
        self.solution = None
        self.subphase = 3
