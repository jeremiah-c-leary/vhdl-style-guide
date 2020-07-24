
from vsg import parser
from vsg.rules import case_item_rule


class rule_013(case_item_rule):
    '''
    Checks the context identifier has proper case.

    '''

    def __init__(self):
        case_item_rule.__init__(self, 'context', '013', parser.context_is_keyword)
