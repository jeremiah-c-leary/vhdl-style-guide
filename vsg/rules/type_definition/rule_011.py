
from vsg import token

from vsg.rules import blank_line_below_line_ending_with_token

lTokens = []
lTokens.append(token.incomplete_type_declaration.semicolon)
lTokens.append(token.full_type_declaration.semicolon)


class rule_011(blank_line_below_line_ending_with_token):
    '''
    Checks for a blank line below the "type" declaration.
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'type', '011', lTokens)
