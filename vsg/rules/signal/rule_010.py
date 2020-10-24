
from vsg.rules import token_case_n_token_after_tokens

from vsg import token

lTokens = []
lTokens.append(token.signal_declaration.colon)


class rule_010(token_case_n_token_after_tokens):
    '''
    Checks the signal type has proper case if it is a VHDL keyword.
    '''

    def __init__(self):
        token_case_n_token_after_tokens.__init__(self, 'signal', '010', 1, lTokens)
        self.disabled = True
        self.bLimitToVhdlKeywords = True
