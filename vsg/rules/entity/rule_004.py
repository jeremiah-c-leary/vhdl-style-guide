
from vsg.rules import case_item_rule
from vsg.token import entity


class rule_004(case_item_rule):
    '''
    Checks the "entity" keyword has proper case.
    '''

    def __init__(self):
        case_item_rule.__init__(self, 'entity', '004', entity.keyword)
        self.regionBegin = entity.keyword
        self.regionEnd = entity.identifier
