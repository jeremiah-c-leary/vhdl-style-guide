
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.semicolon)


class rule_205(blank_line_below_line_ending_with_token):
    '''
    Checks for a blank line below the semicolon at the end of a subprogram_body.
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'subprogram_body', '205', lTokens)
