
from vsg import parser
from vsg.rules import insert_blank_line_above_line_containing_item_rule


class rule_003(insert_blank_line_above_line_containing_item_rule):
    '''
    Checks for a blank line above the "library" keyword.
    '''

    def __init__(self):
        insert_blank_line_above_line_containing_item_rule.__init__(self, 'library', '003', parser.library_keyword)
        self.regionBegin = parser.library_keyword
        self.regionEnd = parser.library_semicolon
