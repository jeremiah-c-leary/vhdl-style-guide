
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.procedure_specification.designator)


class rule_501(token_case_with_prefix_suffix):
    '''
    Checks the procedure designator has proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'procedure', '501', lTokens)
