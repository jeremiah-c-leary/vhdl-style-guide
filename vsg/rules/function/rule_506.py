
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.designator)


class rule_506(token_case_with_prefix_suffix):
    '''
    Checks the function designator in the end procedure has proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'function', '506', lTokens)
