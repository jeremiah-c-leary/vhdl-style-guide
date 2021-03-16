
from vsg import token

from vsg.rules import n_spaces_between_token_pairs_when_bounded_by_tokens

lTokens = []
lTokens.append([token.mode.out_keyword, token.interface_unknown_declaration.subtype_indication])
lTokens.append([token.mode.out_keyword, token.interface_signal_declaration.subtype_indication])
lTokens.append([token.mode.out_keyword, token.interface_constant_declaration.subtype_indication])
lTokens.append([token.mode.out_keyword, token.interface_variable_declaration.subtype_indication])

oStart = token.port_clause.open_parenthesis
oEnd = token.port_clause.close_parenthesis


class rule_008(n_spaces_between_token_pairs_when_bounded_by_tokens):
    '''
    Port rule 008 checks for four spaces after the "in" keyword in a port declaration for "in" ports.
    '''
    def __init__(self):
        n_spaces_between_token_pairs_when_bounded_by_tokens.__init__(self, 'port', '008', 3, lTokens, oStart, oEnd)
        self.solution = 'Change the number of spaces after the *out* keyword to three spaces.'
