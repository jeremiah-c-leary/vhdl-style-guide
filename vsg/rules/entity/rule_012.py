
from vsg.rules import case_item_rule
from vsg.token import entity


class rule_012(case_item_rule):
    '''
    Checks the simple_name has proper case.
    '''

    def __init__(self):
        case_item_rule.__init__(self, 'entity', '012', entity.simple_name)
        self.regionBegin = entity.simple_name
        self.regionEnd = entity.simple_name
