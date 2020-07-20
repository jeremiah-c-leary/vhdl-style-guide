
from vsg import parser
from vsg.rules import new_case_rule


class rule_004(new_case_rule):
    '''
    Checks the context keyword has proper case.

    '''

    def __init__(self):
        new_case_rule.__init__(self, 'context', '004', parser.context_keyword)
