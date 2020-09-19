
from vsg.rules import insert_blank_line_above_line_containing_item_rule

from vsg.token import context_declaration as token


class rule_024(insert_blank_line_above_line_containing_item_rule):
    '''
    Checks for a blank line above the end context declaration.

    '''

    def __init__(self):
        insert_blank_line_above_line_containing_item_rule.__init__(self, 'context', '024', token.end_keyword, False)
        self.regionBegin = token.context_keyword
        self.regionEnd = token.semicolon
