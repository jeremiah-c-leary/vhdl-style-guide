# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import blank_line_below_line_ending_with_token as Rule

lTokens = []
lTokens.append(token.constant_declaration.semicolon)

lAllowTokens = []
lAllowTokens.append(token.constant_declaration.constant_keyword)


class rule_200(Rule):
    """
    This rule checks for a blank line below a constant declaration unless there is another constant definition.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       constant width  : integer := 32;
       signal   height : integer := 4;

       constant width  : integer := 32;
       constant height : integer := 4;

    **Fix**

    .. code-block:: vhdl

       constant width  : integer := 32;
       signal   height : integer := 4;

       constant width  : integer := 32;
       constant height : integer := 4;
    """

    def __init__(self):
        super().__init__(lTokens, lAllowTokens)
        self.disable = True
        self.configuration.remove("style")
