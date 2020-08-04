
from vsg.token import entity
from vsg.rules import space_between_items_rule


class rule_011(space_between_items_rule):
    '''
    Checks for a single space between the entity end keyword and the entityidentifier and is keyword.
    '''

    def __init__(self):
        space_between_items_rule.__init__(self, 'entity', '011', entity.end_keyword, entity.end_entity_keyword)
        self.regionBegin = entity.end_keyword
        self.regionEnd = entity.end_entity_keyword
