
from vsg.token import use_clause
from vsg.rules import case_item_rule


class rule_005(case_item_rule):
    '''
    Checks the "use" keyword has proper case.
    '''
    def __init__(self):
        case_item_rule.__init__(self, 'library', '005', use_clause.keyword)
        self.regionBegin = use_clause.keyword
        self.regionEnd = use_clause.keyword
