
from vsg.rules import insert_item_after_item_rule

from vsg.token import entity_declaration as token


class rule_015(insert_item_after_item_rule):
    '''
    Checks for the context keyword after the end keyword.

    '''
    def __init__(self):
        insert_item_after_item_rule.__init__(self, 'entity', '015', token.end_keyword, token.semicolon, token.end_entity_keyword('entity'))
        self.insert_space = True
        self.regionBegin = token.end_keyword
        self.regionEnd = token.semicolon
