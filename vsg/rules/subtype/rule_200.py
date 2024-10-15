# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import blank_line_below_line_ending_with_token as Rule

lTokens = []
lTokens.append(token.subtype_declaration.semicolon)

lAllowTokens = []
lAllowTokens.append(token.subtype_declaration.subtype_keyword)


class rule_200(Rule):
    """
    This rule checks for a blank line below a **subtype** declaration unless there is another **subtype** declaration.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       subtype counter_t is unsigned(4 downto 0);
       subtype counter is unsigned(4 downto 0);
       constant width : integer := 32;

    **Fix**

    .. code-block:: vhdl

       subtype counter_t is unsigned(4 downto 0);
       subtype counter is unsigned(4 downto 0);

       constant width : integer := 32;
    """

    def __init__(self):
        super().__init__(lTokens, lAllowTokens)
        self.disable = True
        self.configuration.remove("style")
