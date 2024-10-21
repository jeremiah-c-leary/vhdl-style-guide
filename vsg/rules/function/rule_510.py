# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_in_range_bounded_by_tokens

lTokens = []
lTokens.append(token.mode.in_keyword)
lTokens.append(token.mode.out_keyword)
lTokens.append(token.mode.inout_keyword)
lTokens.append(token.mode.buffer_keyword)
lTokens.append(token.mode.linkage_keyword)

oStart = token.function_specification.open_parenthesis
oEnd = token.function_specification.close_parenthesis


class rule_510(token_case_in_range_bounded_by_tokens):
    """
    This rule checks the parameter direction has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

      function overflow (
        a : IN  integer;
        b : OUT integer
      ) return integer;

    **Fix**

    .. code-block:: vhdl

      function overflow (
        a : in  integer;
        b : out integer
      ) return integer;
    """

    def __init__(self):
        super().__init__(lTokens, oStart, oEnd)
        self.groups.append("case::keyword")
