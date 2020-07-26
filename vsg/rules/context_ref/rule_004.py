
from vsg import parser
from vsg.rules import case_item_rule


class rule_004(case_item_rule):
    '''
    Checks the context selected names have proper case.
    '''
    def __init__(self):
        case_item_rule.__init__(self, 'context_ref', '004', parser.context_reference_identifier)
        self.regionBegin = parser.context_reference_keyword
        self.regionEnd = parser.context_reference_semicolon
