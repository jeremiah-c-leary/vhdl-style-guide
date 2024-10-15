# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import blank_line_below_line_ending_with_token

lTokens = []
lTokens.append(token.subtype_declaration.semicolon)


class rule_202(blank_line_below_line_ending_with_token):
    """
    This rule checks for a blank line below the **subtype** declaration.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       subtype counter is unsigned(4 downto 0);
       signal sm : state_machine;

    **Fix**

    .. code-block:: vhdl

       subtype counter is unsigned(4 downto 0);

       signal sm : state_machine;
    """

    def __init__(self):
        super().__init__(lTokens)
