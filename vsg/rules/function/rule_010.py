
from vsg import parser
from vsg import token

from vsg.rules import consistent_token_case

lTokens = []
lTokens.append(token.function_specification.designator)

lIgnore = []
lIgnore.append(parser.whitespace)
lIgnore.append(parser.carriage_return)
lIgnore.append(parser.blank_line)


class rule_010(consistent_token_case):
    '''
    Checks capitalization consistency of function names.
    '''

    def __init__(self):
        consistent_token_case.__init__(self, 'function', '010', lTokens, lIgnore)
