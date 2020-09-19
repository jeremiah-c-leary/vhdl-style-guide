
from vsg.rules import insert_blank_line_above_line_containing_item_rule

from vsg.token import entity_declaration as token


class rule_003(insert_blank_line_above_line_containing_item_rule):
    '''
    Checks for a blank line above the "entity" keyword.
    '''

    def __init__(self):
        insert_blank_line_above_line_containing_item_rule.__init__(self, 'entity', '003', token.entity_keyword)
        self.regionBegin = token.entity_keyword
        self.regionEnd = token.identifier
