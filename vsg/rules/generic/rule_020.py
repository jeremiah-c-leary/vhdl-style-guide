
from vsg.rules import token_prefix_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.interface_constant_declaration.identifier)
lTokens.append(token.interface_signal_declaration.identifier)
lTokens.append(token.interface_variable_declaration.identifier)
lTokens.append(token.interface_unknown_declaration.identifier)


class rule_020(token_prefix_between_tokens):
    '''
    Checks for prefixes in generic names.
    '''

    def __init__(self):
        token_prefix_between_tokens.__init__(self, 'generic', '020', lTokens, token.generic_clause.open_parenthesis, token.generic_clause.close_parenthesis)
        self.prefixes = ['g_']
