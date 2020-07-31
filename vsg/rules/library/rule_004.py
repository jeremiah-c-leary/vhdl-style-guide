
from vsg import parser
from vsg.rules import case_item_rule


class rule_004(case_item_rule):
    '''
    Checks the "library" keyword has proper case.
    '''
    def __init__(self):
        case_item_rule.__init__(self, 'library', '004', parser.library_keyword)
        self.regionBegin = parser.library_keyword
        self.regionEnd = parser.library_semicolon
