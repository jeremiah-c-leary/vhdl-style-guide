
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.subprogram_declaration.semicolon)
lTokens.append(token.subprogram_body.semicolon)


class rule_007(blank_line_below_line_ending_with_token):
    '''
    Function rule 007 enforces a blank line below the ;.
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'function', '007', lTokens)
