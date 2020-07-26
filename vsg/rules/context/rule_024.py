
from vsg import parser
from vsg.rules import insert_blank_line_above_line_containing_item_rule


class rule_024(insert_blank_line_above_line_containing_item_rule):
    '''
    Checks for a blank line above the end context declaration.

    '''

    def __init__(self):
        insert_blank_line_above_line_containing_item_rule.__init__(self, 'context', '024', parser.context_end_keyword, False)
        self.regionBegin = parser.context_keyword
        self.regionEnd = parser.context_semicolon
