
from vsg import parser
from vsg.rules import space_between_items_rule


class rule_002(space_between_items_rule):
    '''
    Checks for a single space between the context keyword and the context identifier

    '''
    def __init__(self):
        space_between_items_rule.__init__(self, 'context_ref', '002', parser.context_reference_keyword, parser.context_reference_identifier, 'context keyword')
        self.regionBegin = parser.context_reference_keyword
        self.regionEnd = parser.context_reference_semicolon
