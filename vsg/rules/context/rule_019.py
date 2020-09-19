
from vsg.rules import space_between_items_rule

from vsg.token import context_declaration as token


class rule_019(space_between_items_rule):
    '''
    Checks for a single space between the context keyword and the context identifier in the end context portion of a context declaration.

    '''

    def __init__(self):
        space_between_items_rule.__init__(self, 'context', '019', token.end_context_keyword, token.context_simple_name)
        self.regionBegin = token.context_keyword
        self.regionEnd = token.semicolon
