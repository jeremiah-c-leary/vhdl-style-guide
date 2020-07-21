
from vsg import parser
from vsg.rules import move_item_next_to_another_item_rule


class rule_005(move_item_next_to_another_item_rule):
    '''
    Checks the context identifier is on the same line as the context keyword.

    '''

    def __init__(self):
        move_item_next_to_another_item_rule.__init__(self, 'context', '005', parser.context_keyword, parser.context_identifier)
        self.solution = None
        self.subphase = 1
