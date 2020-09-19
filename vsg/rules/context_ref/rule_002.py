
from vsg import parser

from vsg.token import context_reference as token

from vsg.rules import space_between_items_rule


class rule_002(space_between_items_rule):
    '''
    Checks for a single space between the context keyword and the context identifier

    '''
    def __init__(self):
        space_between_items_rule.__init__(self, 'context_ref', '002', token.keyword, token.selected_name)
        self.regionBegin = token.keyword
        self.regionEnd = token.semicolon
