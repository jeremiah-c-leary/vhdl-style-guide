
from vsg.rules import token_case_in_range_bounded_by_tokens_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.designator)

oStartToken = token.function_specification.function_keyword
oEndToken = token.subprogram_body.semicolon


class rule_506(token_case_in_range_bounded_by_tokens_with_prefix_suffix):
    '''
    Checks the function designator in the end procedure has proper case.
    '''

    def __init__(self):
        token_case_in_range_bounded_by_tokens_with_prefix_suffix.__init__(self, 'function', '506', lTokens, oStartToken, oEndToken)
