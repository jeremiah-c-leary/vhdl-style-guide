# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_in_range_bounded_by_tokens

lTokens = []
lTokens.append(token.parameter_specification.in_keyword)

oStartToken = token.for_generate_statement.for_keyword
oEndToken = token.for_generate_statement.generate_keyword


class rule_502(token_case_in_range_bounded_by_tokens):
    """
    This rule checks the **in** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       gen_label : for lv_thing IN t_thing generate

    **Fix**

    .. code-block:: vhdl

       gen_label : for lv_thing in t_thing generate
    """

    def __init__(self):
        super().__init__(lTokens, oStartToken, oEndToken)
        self.groups.append("case::keyword")
