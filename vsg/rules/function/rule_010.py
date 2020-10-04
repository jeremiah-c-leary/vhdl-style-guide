
from vsg.rules import consistent_token_case

from vsg import token


class rule_010(consistent_token_case):
    '''
    Checks capitalization consistency of function names.
    '''

    def __init__(self):
        consistent_token_case.__init__(self, 'function', '010', [token.function_specification.designator])
