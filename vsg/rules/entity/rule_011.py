
from vsg.rules import space_between_items_rule

from vsg.token import entity_declaration as token


class rule_011(space_between_items_rule):
    '''
    Checks for a single space between the entity end keyword and the entityidentifier and is keyword.
    '''

    def __init__(self):
        space_between_items_rule.__init__(self, 'entity', '011', token.end_keyword, token.end_entity_keyword)
        self.regionBegin = token.end_keyword
        self.regionEnd = token.end_entity_keyword
