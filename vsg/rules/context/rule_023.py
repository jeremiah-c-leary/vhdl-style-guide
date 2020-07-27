
from vsg import parser
from vsg.rules import insert_blank_line_below_line_containing_item_rule


class rule_023(insert_blank_line_below_line_containing_item_rule):
    '''
    Checks for a single space between the context keyword and the context identifier

    '''

    def __init__(self):
        insert_blank_line_below_line_containing_item_rule.__init__(self, 'context', '023', parser.context_is_keyword)
        self.regionBegin = parser.context_keyword
        self.regionEnd = parser.context_semicolon
