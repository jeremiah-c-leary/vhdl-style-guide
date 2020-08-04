
from vsg.token import entity
from vsg.rules import space_between_items_rule


class rule_007(space_between_items_rule):
    '''
    Entity rule 007 checks for a single space between the entity identifier and is keyword.
    '''

    def __init__(self):
        space_between_items_rule.__init__(self, 'entity', '007', entity.identifier, entity.is_keyword)
        self.regionBegin = entity.identifier
        self.regionEnd = entity.is_keyword
