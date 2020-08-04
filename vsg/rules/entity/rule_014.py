
from vsg.rules import case_item_rule
from vsg.token import entity


class rule_014(case_item_rule):
    '''
    Checks the end entity keyword has proper case.
    '''

    def __init__(self):
        case_item_rule.__init__(self, 'entity', '014', entity.end_entity_keyword)
        self.regionBegin = entity.end_entity_keyword
        self.regionEnd = entity.end_entity_keyword
