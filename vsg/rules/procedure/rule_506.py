
from vsg.rules import token_case_in_range_bounded_by_tokens

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.designator)

oStartToken = token.procedure_specification.procedure_keyword
oEndToken = token.subprogram_body.semicolon


class rule_506(token_case_in_range_bounded_by_tokens):
    '''
    Checks the procedure designator in the end procedure has proper case.
    '''

    def __init__(self):
        token_case_in_range_bounded_by_tokens.__init__(self, 'procedure', '506', lTokens, oStartToken, oEndToken)
