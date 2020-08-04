
from vsg.rules import case_item_rule
from vsg.token import entity


class rule_008(case_item_rule):
    '''
    Checks the entity identifier has proper case.
    '''

    def __init__(self):
        case_item_rule.__init__(self, 'entity', '008', entity.identifier)
        self.regionBegin = entity.identifier
        self.regionEnd = entity.identifier
