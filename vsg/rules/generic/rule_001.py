
from vsg.rules import blank_line_above_line_starting_with_token

from vsg.token import generic_clause as token

lTokens = []
lTokens.append(token.generic_keyword)

class rule_001(blank_line_above_line_starting_with_token):
    '''
    Checks for more than one blank line above the *generic* keyword.

    '''
    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'generic', '001', lTokens)
        self.style = 'no_blank_line'
