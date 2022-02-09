
from vsg.rules import token_case_in_range_bounded_by_tokens

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.begin_keyword)

oStartToken = token.procedure_specification.procedure_keyword
oEndToken = token.subprogram_body.semicolon


class rule_503(token_case_in_range_bounded_by_tokens):
    '''
    This rule checks the **begin** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       procedure average_samples is
       BEGIN

    **Fix**

    .. code-block:: vhdl

       procedure average_samples is
       begin
    '''

    def __init__(self):
        token_case_in_range_bounded_by_tokens.__init__(self, 'procedure', '503', lTokens, oStartToken, oEndToken)
        self.groups.append('case::keyword')
