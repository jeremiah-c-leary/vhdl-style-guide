
from vsg.rules import previous_line

from vsg.token import function_specification as token

lTokens = []
lTokens.append(token.function_keyword)
lTokens.append(token.pure_keyword)
lTokens.append(token.impure_keyword)


class rule_006(previous_line):
    '''
    Checks for a blank line above the "function" keyword.
    '''

    def __init__(self):
        previous_line.__init__(self, 'function', '006', lTokens)
