
from vsg import parser
from vsg.rules import space_between_items_rule


class rule_018(space_between_items_rule):
    '''
    Checks for a single space between the end keyword and the context keyword.

    '''

    def __init__(self):
        space_between_items_rule.__init__(self, 'context', '018', parser.context_end_keyword, parser.context_end_context_keyword, 'end keyword')
        self.regionBegin = parser.context_keyword
        self.regionEnd = parser.context_semicolon
