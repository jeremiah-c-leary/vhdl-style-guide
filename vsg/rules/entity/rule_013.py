
from vsg.token import entity
from vsg.rules import space_between_items_rule


class rule_013(space_between_items_rule):
    '''
    Checks for a single space between the end entity keyword and the entity simple_name.
    '''

    def __init__(self):
        space_between_items_rule.__init__(self, 'entity', '013', entity.end_entity_keyword, entity.simple_name)
        self.regionBegin = entity.end_entity_keyword
        self.regionEnd = entity.simple_name
