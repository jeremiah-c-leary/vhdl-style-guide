
from vsg import parser
from vsg.rules import new_case_rule


class rule_012(new_case_rule):
    '''
    Checks the context identifier has proper case.

    '''

    def __init__(self):
        new_case_rule.__init__(self, 'context', '012', parser.context_identifier)
