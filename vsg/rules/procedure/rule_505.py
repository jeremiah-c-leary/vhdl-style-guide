# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_in_range_bounded_by_tokens

lTokens = []
lTokens.append(token.subprogram_kind.procedure_keyword)

oStartToken = token.subprogram_body.end_keyword
oEndToken = token.subprogram_body.semicolon

class rule_505(token_case_in_range_bounded_by_tokens):
    """
    This rule checks the **procedure** keyword in the **end procedure** has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       end PROCEDURE average_samples;

    **Fix**

    .. code-block:: vhdl

       end procedure average_samples;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
