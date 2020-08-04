
from vsg.token import entity
from vsg.rules import copy_item_value_and_insert_new_item_after_item_rule


class rule_019(copy_item_value_and_insert_new_item_after_item_rule):
    '''
    Checks for the context keyword after the end keyword.

    '''

    def __init__(self):
        copy_item_value_and_insert_new_item_after_item_rule.__init__(self, 'entity', '019', entity.end_entity_keyword, entity.semicolon, entity.identifier, entity.simple_name('unknown'))
        self.subphase = 2
        self.regionBegin = entity.identifier
        self.regionEnd = entity.semicolon
