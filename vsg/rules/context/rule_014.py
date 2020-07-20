
from vsg import parser
from vsg.rules import new_case_rule


class rule_014(new_case_rule):
    '''
    Checks the context identifier has proper case.

    '''

    def __init__(self):
        new_case_rule.__init__(self, 'context', '014', parser.context_end_keyword)
