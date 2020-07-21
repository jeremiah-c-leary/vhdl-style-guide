
from vsg import parser
from vsg.rules import copy_item_value_and_insert_new_item_after_item_rule


class rule_022(copy_item_value_and_insert_new_item_after_item_rule):
    '''
    Checks for the context keyword after the end keyword.

    '''

    def __init__(self):
        copy_item_value_and_insert_new_item_after_item_rule.__init__(self, 'context', '022', parser.context_end_context_keyword, parser.context_semicolon, parser.context_identifier, parser.context_end_identifier('unknown'))
        self.solution = 'missing context identifier'
