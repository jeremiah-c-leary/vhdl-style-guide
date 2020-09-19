
from vsg.rules import copy_item_value_and_insert_new_item_after_item_rule

from vsg.token import entity_declaration as token


class rule_019(copy_item_value_and_insert_new_item_after_item_rule):
    '''
    Checks for the context keyword after the end keyword.

    '''

    def __init__(self):
        copy_item_value_and_insert_new_item_after_item_rule.__init__(self, 'entity', '019', token.end_entity_keyword, token.semicolon, token.identifier, token.entity_simple_name('unknown'))
        self.subphase = 2
        self.regionBegin = token.identifier
        self.regionEnd = token.semicolon
