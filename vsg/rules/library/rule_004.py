
from vsg.rules import case_item_rule

from vsg.token import library_clause as token


class rule_004(case_item_rule):
    '''
    Checks the "library" keyword has proper case.
    '''
    def __init__(self):
        case_item_rule.__init__(self, 'library', '004', token.keyword)
        self.regionBegin = token.keyword
        self.regionEnd = token.semicolon
