
from vsg import parser
from vsg.rules import space_between_items_rule


class rule_002(space_between_items_rule):
    '''
    Checks for a single space between the library keyword and the library logical name

    '''
    def __init__(self):
        space_between_items_rule.__init__(self, 'library', '002', parser.library_keyword, parser.library_logical_name)
        self.regionBegin = parser.library_keyword
        self.regionEnd = parser.library_semicolon
