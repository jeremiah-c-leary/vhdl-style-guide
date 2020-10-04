
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.function_specification.pure_keyword)
lTokens.append(token.function_specification.impure_keyword)
lTokens.append(token.function_specification.function_keyword)


class rule_001(token_indent):
    '''
    Checks for the proper indentation at the beginning of the function specification.
    '''

    def __init__(self):
        token_indent.__init__(self, 'function', '001', lTokens)
