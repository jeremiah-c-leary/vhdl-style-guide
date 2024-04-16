# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_in_range_bounded_by_tokens

lTokens = []
lTokens.append(token.subprogram_body.is_keyword)

oStartToken = token.function_specification.function_keyword
oEndToken = token.subprogram_body.semicolon


class rule_502(token_case_in_range_bounded_by_tokens):
    """
    This rule checks the **is** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       function overflow (a: integer) return integer IS

    **Fix**

    .. code-block:: vhdl

       function overflow (a: integer) return integer is
    """

    def __init__(self):
        super().__init__(lTokens, oStartToken, oEndToken)
        self.groups.append("case::keyword")
