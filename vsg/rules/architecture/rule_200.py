# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import blank_line_below_line_ending_with_token

lTokens = []
lTokens.append(token.architecture_body.semicolon)


class rule_200(blank_line_below_line_ending_with_token):
    """
    This rule checks for a blank line below the end architecture statement.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       end architecture;
       library ieee;

    **Fix**

    .. code-block:: vhdl

       end architecture;

       library ieee;
    """

    def __init__(self):
        super().__init__(lTokens)
