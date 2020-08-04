
from vsg.token import entity
from vsg.rules import move_item_next_to_another_item_rule


class rule_005(move_item_next_to_another_item_rule):
    '''
    Checks the is keyword is on the same line as the context identifier.

    '''

    def __init__(self):
        move_item_next_to_another_item_rule.__init__(self, 'entity', '005', entity.identifier, entity.is_keyword)
        self.subphase = 2
        self.regionBegin = entity.identifier
        self.regionEnd = entity.is_keyword
