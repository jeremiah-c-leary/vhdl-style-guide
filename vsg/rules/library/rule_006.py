
from vsg import parser
from vsg.rules import space_between_items_rule


class rule_006(space_between_items_rule):
    '''
    Checks for a single space between the use keyword and the use logical name

    '''
    def __init__(self):
        space_between_items_rule.__init__(self, 'library', '006', parser.use_keyword, parser.use_selected_name)
        self.regionBegin = parser.use_keyword
        self.regionEnd = parser.use_semicolon
