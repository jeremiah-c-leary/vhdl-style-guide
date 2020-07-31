
from vsg import parser
from vsg.rules import case_item_rule


class rule_005(case_item_rule):
    '''
    Checks the "use" keyword has proper case.
    '''
    def __init__(self):
        case_item_rule.__init__(self, 'library', '005', parser.use_keyword)
        self.regionBegin = parser.use_keyword
        self.regionEnd = parser.use_semicolon
