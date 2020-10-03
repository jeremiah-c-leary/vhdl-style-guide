
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.loop_statement.loop_label)


class rule_003(token_case):
    '''
    For Loop rule 003 checks the label has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'for_loop', '003', lTokens)
