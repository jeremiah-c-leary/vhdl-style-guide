
from vsg.rules import remove_blank_lines_below_item_rule

from vsg.token import context_declaration as token


class rule_026(remove_blank_lines_below_item_rule):
    '''
    Checks for a single space between the context keyword and the context identifier

    '''
    def __init__(self):
        remove_blank_lines_below_item_rule.__init__(self, 'context', '026', token.is_keyword)
        self.regionBegin = token.context_keyword
        self.regionEnd = token.semicolon
