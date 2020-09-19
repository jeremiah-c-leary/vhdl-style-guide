
from vsg.rules import case_item_rule

from vsg.token import entity_declaration as token


class rule_004(case_item_rule):
    '''
    Checks the "entity" keyword has proper case.
    '''

    def __init__(self):
        case_item_rule.__init__(self, 'entity', '004', token.entity_keyword)
        self.regionBegin = token.entity_keyword
        self.regionEnd = token.identifier
