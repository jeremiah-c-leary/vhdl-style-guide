
from vsg.rules import space_between_items_rule

from vsg.token import context_declaration as token


class rule_002(space_between_items_rule):
    '''
    Checks for a single space between the context keyword and the context identifier

    '''
    def __init__(self):
        space_between_items_rule.__init__(self, 'context', '002', token.context_keyword, token.identifier)
        self.regionBegin = token.context_keyword
        self.regionEnd = token.semicolon
