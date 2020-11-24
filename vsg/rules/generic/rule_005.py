
from vsg import token

from vsg.rules import single_space_between_token_pairs_bounded_by_tokens

lTokens = []
lTokens.append([token.interface_constant_declaration.colon, token.interface_constant_declaration.subtype_indication])
lTokens.append([token.interface_signal_declaration.colon, token.interface_signal_declaration.subtype_indication])
lTokens.append([token.interface_variable_declaration.colon, token.interface_variable_declaration.subtype_indication])
lTokens.append([token.interface_file_declaration.colon, token.interface_file_declaration.subtype_indication])
lTokens.append([token.interface_unknown_declaration.colon, token.interface_unknown_declaration.subtype_indication])

lStart = token.generic_clause.open_parenthesis
lEnd = token.generic_clause.close_parenthesis


class rule_005(single_space_between_token_pairs_bounded_by_tokens):
    '''
    Checks for a single space between the : and identifier.
    '''
    def __init__(self):
        single_space_between_token_pairs_bounded_by_tokens.__init__(self, 'generic', '005', lTokens, lStart, lEnd)
        self.solution = 'Reduce number of spaces after the colon to 1.'
