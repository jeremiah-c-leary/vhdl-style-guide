
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.is_keyword)

lAllowTokens = []
lAllowTokens.append(token.subprogram_body.begin_keyword)


class rule_201(blank_line_below_line_ending_with_token):
    '''
    Checks for a blank line below the opening section of a procedure specification.
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'procedure', '201', lTokens, lAllowTokens)
