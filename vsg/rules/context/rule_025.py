
from vsg.rules import insert_blank_line_below_line_containing_item_rule

from vsg.token import context_declaration as token


class rule_025(insert_blank_line_below_line_containing_item_rule):
    '''
    Checks for a single space between the context keyword and the context identifier

    '''

    def __init__(self):
        insert_blank_line_below_line_containing_item_rule.__init__(self, 'context', '025', token.semicolon)
        self.regionBegin = token.context_keyword
        self.regionEnd = token.semicolon
