
from vsg.rules import token_case_n_token_after_tokens_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.interface_constant_declaration.colon)
lTokens.append(token.interface_variable_declaration.colon)
lTokens.append(token.interface_signal_declaration.colon)
lTokens.append(token.interface_unknown_declaration.colon)

oStart = token.port_clause.open_parenthesis
oEnd = token.port_clause.close_parenthesis


class rule_018(token_case_n_token_after_tokens_between_tokens):
    '''
    Checks the port type has proper case if it is a VHDL keyword.
    '''

    def __init__(self):
        token_case_n_token_after_tokens_between_tokens.__init__(self, 'port', '018', 2, lTokens, oStart, oEnd, True)
        self.disabled = True
