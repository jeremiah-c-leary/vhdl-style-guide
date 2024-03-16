# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_in_range_bounded_by_tokens

lTokens = []
lTokens.append(token.mode.in_keyword)
lTokens.append(token.mode.out_keyword)
lTokens.append(token.mode.inout_keyword)
lTokens.append(token.mode.buffer_keyword)
lTokens.append(token.mode.linkage_keyword)

oStart = token.port_clause.open_parenthesis
oEnd = token.port_clause.close_parenthesis


class rule_019(token_case_in_range_bounded_by_tokens):
    """
    This rule checks the port direction has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       port (
         WR_EN    : IN    std_logic;
         RD_EN    : in    std_logic;
         OVERFLOW : OUT   std_logic;
         DATA     : INOUT std_logic
       );

    **Fix**

    .. code-block:: vhdl

       port (
         WR_EN    : in    std_logic;
         RD_EN    : in    std_logic;
         OVERFLOW : out   std_logic;
         DATA     : inout std_logic
       );
    """

    def __init__(self):
        super().__init__(lTokens, oStart, oEnd)
        self.groups.append("case::keyword")
