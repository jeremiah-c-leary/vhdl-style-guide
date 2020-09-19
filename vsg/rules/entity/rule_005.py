
from vsg.rules import move_item_next_to_another_item_rule

from vsg.token import entity_declaration as token


class rule_005(move_item_next_to_another_item_rule):
    '''
    Checks the is keyword is on the same line as the context identifier.

    '''

    def __init__(self):
        move_item_next_to_another_item_rule.__init__(self, 'entity', '005', token.identifier, token.is_keyword)
        self.subphase = 2
        self.regionBegin = token.identifier
        self.regionEnd = token.is_keyword
