
from vsg.rules import token_case_in_range_bounded_by_tokens

from vsg import token

lTokens = []
lTokens.append(token.interface_constant_declaration.identifier)
lTokens.append(token.interface_signal_declaration.identifier)
lTokens.append(token.interface_variable_declaration.identifier)
lTokens.append(token.interface_unknown_declaration.identifier)


class rule_010(token_case_in_range_bounded_by_tokens):
    '''
    Checks for casee in port identifiers.
    '''

    def __init__(self):
        token_case_in_range_bounded_by_tokens.__init__(self, 'port', '010', lTokens, token.port_clause.open_parenthesis, token.port_clause.close_parenthesis)
