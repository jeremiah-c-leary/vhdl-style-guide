
from vsg import parser
from vsg.rules import insert_item_after_item_rule


class rule_021(insert_item_after_item_rule):
    '''
    Checks for the context keyword after the end keyword.

    '''

    def __init__(self):
        insert_item_after_item_rule.__init__(self, 'context', '021', parser.context_end_keyword, parser.context_semicolon, parser.context_end_context_keyword('context'))
