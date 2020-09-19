
from vsg.rules import space_between_items_rule

from vsg.token import entity_declaration as token


class rule_013(space_between_items_rule):
    '''
    Checks for a single space between the end entity keyword and the entity simple_name.
    '''

    def __init__(self):
        space_between_items_rule.__init__(self, 'entity', '013', token.end_entity_keyword, token.entity_simple_name)
        self.regionBegin = token.end_entity_keyword
        self.regionEnd = token.entity_simple_name
