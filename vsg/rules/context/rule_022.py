
from vsg.rules import copy_item_value_and_insert_new_item_after_item_rule

from vsg.token import context_declaration as token


class rule_022(copy_item_value_and_insert_new_item_after_item_rule):
    '''
    Checks for the context keyword after the end keyword.

    '''

    def __init__(self):
        copy_item_value_and_insert_new_item_after_item_rule.__init__(self, 'context', '022', token.end_context_keyword, token.semicolon, token.identifier, token.context_simple_name('unknown'))
        self.solution = 'missing context identifier'
        self.subphase = 2
        self.regionBegin = token.context_keyword
        self.regionEnd = token.semicolon
