
from vsg import parser
from vsg.rules import move_item_rule


class rule_006(move_item_rule):
    '''
    Checks the context identifier is on the same line as the context keyword.

    '''

    def __init__(self):
        move_item_rule.__init__(self, 'context', '006', parser.context_identifier, parser.context_is_keyword)
        self.solution = None
        self.subphase = 2
