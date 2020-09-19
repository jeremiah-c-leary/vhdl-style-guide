
from vsg.rules import case_item_rule

from vsg.token import entity_declaration as token


class rule_012(case_item_rule):
    '''
    Checks the entity_simple_name has proper case.
    '''

    def __init__(self):
        case_item_rule.__init__(self, 'entity', '012', token.entity_simple_name)
        self.regionBegin = token.entity_simple_name
        self.regionEnd = token.entity_simple_name
