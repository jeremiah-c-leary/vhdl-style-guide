from vsg.rules import case_item_rule
from vsg.token import entity


class rule_006(case_item_rule):
    '''
    Checks the "is" keyword has proper case.
    '''

    def __init__(self):
        case_item_rule.__init__(self, 'entity', '006', entity.is_keyword)
        self.regionBegin = entity.is_keyword
        self.regionEnd = entity.is_keyword
