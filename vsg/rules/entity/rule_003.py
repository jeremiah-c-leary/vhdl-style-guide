
from vsg.token import entity
from vsg.rules import insert_blank_line_above_line_containing_item_rule


class rule_003(insert_blank_line_above_line_containing_item_rule):
    '''
    Checks for a blank line above the "entity" keyword.
    '''

    def __init__(self):
        insert_blank_line_above_line_containing_item_rule.__init__(self, 'entity', '003', entity.keyword)
        self.regionBegin = entity.keyword
        self.regionEnd = entity.identifier
