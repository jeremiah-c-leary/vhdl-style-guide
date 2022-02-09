
from vsg.rules import token_case_in_range_bounded_by_tokens_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.designator)

oStartToken = token.procedure_specification.procedure_keyword
oEndToken = token.subprogram_body.semicolon


class rule_506(token_case_in_range_bounded_by_tokens_with_prefix_suffix):
    '''
    This rule checks the procedure designator has proper case on the end procedure declaration.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       end procedure AVERAGE_SAMPLES;

    **Fix**

    .. code-block:: vhdl

       end procedure average_samples;
    '''

    def __init__(self):
        token_case_in_range_bounded_by_tokens_with_prefix_suffix.__init__(self, 'procedure', '506', lTokens, oStartToken, oEndToken)
        self.groups.append('case::name')
