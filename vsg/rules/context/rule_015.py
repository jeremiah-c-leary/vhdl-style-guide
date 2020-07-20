
from vsg import parser
from vsg.rules import new_case_rule


class rule_015(new_case_rule):
    '''
    Checks the context identifier has proper case.

    '''

    def __init__(self):
        new_case_rule.__init__(self, 'context', '015', parser.context_end_context_keyword)
