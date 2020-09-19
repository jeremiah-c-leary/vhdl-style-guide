
from vsg.rules import space_between_items_rule

from vsg.token import entity_declaration as token


class rule_002(space_between_items_rule):
    '''
    Entity rule 002 checks for a single space between the entity keyword and token identifier.
    '''

    def __init__(self):
        space_between_items_rule.__init__(self, 'entity', '002', token.entity_keyword, token.identifier)
        self.regionBegin = token.entity_keyword
        self.regionEnd = token.identifier
