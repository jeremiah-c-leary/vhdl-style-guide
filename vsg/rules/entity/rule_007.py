
from vsg.rules import space_between_items_rule

from vsg.token import entity_declaration as token


class rule_007(space_between_items_rule):
    '''
    Entity rule 007 checks for a single space between the entity identifier and is keyword.
    '''

    def __init__(self):
        space_between_items_rule.__init__(self, 'entity', '007', token.identifier, token.is_keyword)
        self.regionBegin = token.identifier
        self.regionEnd = token.is_keyword
