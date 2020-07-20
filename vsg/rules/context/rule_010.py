
from vsg import parser
from vsg.rules import move_item_rule


class rule_010(move_item_rule):
    '''
    Checks the context keyword is on the same line as the end context keyword.

    '''

    def __init__(self):
        move_item_rule.__init__(self, 'context', '010', parser.context_end_context_keyword, parser.context_end_identifier)
        self.solution = None
        self.subphase = 2
