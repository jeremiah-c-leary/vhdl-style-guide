
from vsg.rules import blank_line_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.begin_keyword)

lAllowTokens = []
lAllowTokens.append(token.subprogram_body.is_keyword)

class rule_202(blank_line_above_line_starting_with_token):
    '''
    Checks for a blank line above the begin keyword.
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'function', '202', lTokens, lAllowTokens)
