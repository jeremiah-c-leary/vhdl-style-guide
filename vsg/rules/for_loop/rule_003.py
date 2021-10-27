
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.loop_statement.loop_label)


class rule_003(token_case_with_prefix_suffix):
    '''
    For Loop rule 003 checks the label has proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'for_loop', '003', lTokens)
