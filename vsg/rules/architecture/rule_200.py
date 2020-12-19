
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.architecture_body.semicolon)


class rule_200(blank_line_below_line_ending_with_token):
    '''
    Checks for a blank line below the package keyword.
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'architecture', '200', lTokens)
