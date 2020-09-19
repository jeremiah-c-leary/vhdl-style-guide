
from vsg.rules import space_between_items_rule

from vsg.token import context_declaration as token


class rule_017(space_between_items_rule):
    '''
    Checks for a single space between the context identifier and the is keyword

    '''

    def __init__(self):
        space_between_items_rule.__init__(self, 'context', '017', token.identifier, token.is_keyword)
        self.regionBegin = token.context_keyword
        self.regionEnd = token.semicolon
