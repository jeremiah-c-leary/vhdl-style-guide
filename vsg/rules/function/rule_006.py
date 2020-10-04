
from vsg.rules import blank_line_above_line_starting_with_token

from vsg.token import function_specification as token

lTokens = []
lTokens.append(token.function_keyword)
lTokens.append(token.pure_keyword)
lTokens.append(token.impure_keyword)


class rule_006(blank_line_above_line_starting_with_token):
    '''
    Checks for a blank line above the "function" keyword.
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'function', '006', lTokens)
