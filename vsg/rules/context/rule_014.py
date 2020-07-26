
from vsg import parser
from vsg.rules import case_item_rule


class rule_014(case_item_rule):
    '''
    Checks the context identifier has proper case.

    '''

    def __init__(self):
        case_item_rule.__init__(self, 'context', '014', parser.context_end_keyword)
        self.regionBegin = parser.context_keyword
        self.regionEnd = parser.context_semicolon
