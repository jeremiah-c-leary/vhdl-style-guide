
from vsg.rules import token_suffix_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.interface_constant_declaration.identifier)
lTokens.append(token.interface_signal_declaration.identifier)
lTokens.append(token.interface_variable_declaration.identifier)
lTokens.append(token.interface_unknown_declaration.identifier)


class rule_025(token_suffix_between_tokens):
    '''
    Checks for suffixes in port names.
    '''

    def __init__(self):
        token_suffix_between_tokens.__init__(self, 'port', '025', lTokens, token.port_clause.open_parenthesis, token.port_clause.close_parenthesis)
        self.suffixes = ['_i', '_o', '_io']
