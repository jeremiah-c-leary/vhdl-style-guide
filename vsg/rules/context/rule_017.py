
from vsg import parser
from vsg.rules import space_between_items_rule


class rule_017(space_between_items_rule):
    '''
    Checks for a single space between the context identifier and the is keyword

    '''

    def __init__(self):
        space_between_items_rule.__init__(self, 'context', '017', parser.context_identifier, parser.context_is_keyword)
        self.regionBegin = parser.context_keyword
        self.regionEnd = parser.context_semicolon
