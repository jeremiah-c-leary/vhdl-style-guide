
from vsg.token import entity
from vsg.rules import insert_item_after_item_rule


class rule_015(insert_item_after_item_rule):
    '''
    Checks for the context keyword after the end keyword.

    '''
    def __init__(self):
        insert_item_after_item_rule.__init__(self, 'entity', '015', entity.end_keyword, entity.semicolon, entity.end_entity_keyword('entity'))
        self.insert_space = True
        self.regionBegin = entity.end_keyword
        self.regionEnd = entity.semicolon
