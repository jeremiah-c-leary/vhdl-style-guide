
from vsg import parser
from vsg.rules import space_between_items_rule


class rule_019(space_between_items_rule):
    '''
    Checks for a single space between the context keyword and the context identifier in the end context portion of a context declaration.

    '''

    def __init__(self):
        space_between_items_rule.__init__(self, 'context', '019', parser.context_end_context_keyword, parser.context_end_identifier, 'end keyword')
        self.regionBegin = parser.context_keyword
        self.regionEnd = parser.context_semicolon
