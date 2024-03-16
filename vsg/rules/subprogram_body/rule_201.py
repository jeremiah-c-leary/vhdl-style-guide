# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import blank_line_below_line_ending_with_token

lTokens = []
lTokens.append(token.subprogram_body.is_keyword)

lAllowTokens = []
lAllowTokens.append(token.subprogram_body.begin_keyword)


class rule_201(blank_line_below_line_ending_with_token):
    """
    This rule checks for a blank line below the **is** keyword.

    This rule allows the **begin** keyword to occupy the blank line:

    .. code-block:: vhdl

       function overflow (a: integer) return integer is
       begin

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       function overflow (a: integer) return integer is
         constant width : integer := 32;
       begin

    **Fix**

    .. code-block:: vhdl

       function overflow (a: integer) return integer is

         constant width : integer := 32;
       begin
    """

    def __init__(self):
        super().__init__(lTokens, lAllowTokens)
