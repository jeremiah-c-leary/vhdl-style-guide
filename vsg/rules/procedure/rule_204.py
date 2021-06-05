
from vsg.rules import blank_line_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.end_keyword)


class rule_204(blank_line_above_line_starting_with_token):
    '''
    Checks for a blank line above the end keyword.
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'procedure', '204', lTokens)
