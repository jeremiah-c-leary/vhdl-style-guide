
from vsg.rules import token_case_in_range_bounded_by_tokens

from vsg import token

lTokens = []
lTokens.append(token.interface_constant_declaration.identifier)
lTokens.append(token.interface_signal_declaration.identifier)
lTokens.append(token.interface_variable_declaration.identifier)
lTokens.append(token.interface_file_declaration.identifier)
lTokens.append(token.interface_unknown_declaration.identifier)

oStart = token.generic_clause.open_parenthesis
oEnd = token.generic_clause.close_parenthesis


class rule_007(token_case_in_range_bounded_by_tokens):
    '''
    Checks the "generic" keyword has proper case.
    '''

    def __init__(self):
        token_case_in_range_bounded_by_tokens.__init__(self, 'generic', '007', lTokens, oStart, oEnd)
