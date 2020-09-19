
from vsg.rules import insert_blank_line_above_line_containing_item_rule

from vsg.token import library_clause as token


class rule_003(insert_blank_line_above_line_containing_item_rule):
    '''
    Checks for a blank line above the "library" keyword.
    '''

    def __init__(self):
        insert_blank_line_above_line_containing_item_rule.__init__(self, 'library', '003', token.keyword)
        self.regionBegin = token.keyword
        self.regionEnd = token.semicolon
