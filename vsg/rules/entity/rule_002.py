
from vsg.token import entity
from vsg.rules import space_between_items_rule


class rule_002(space_between_items_rule):
    '''
    Entity rule 002 checks for a single space between the entity keyword and entity identifier.
    '''

    def __init__(self):
        space_between_items_rule.__init__(self, 'entity', '002', entity.keyword, entity.identifier)
        self.regionBegin = entity.keyword
        self.regionEnd = entity.identifier
