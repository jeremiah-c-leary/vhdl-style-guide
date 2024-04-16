# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import remove_excessive_blank_lines_above_line_starting_with_token

lTokens = []
lTokens.append(token.if_statement.else_keyword)

lOverrides = []
lOverrides.append(token.case_statement.semicolon)
lOverrides.append(token.loop_statement.semicolon)


class rule_010(remove_excessive_blank_lines_above_line_starting_with_token):
    """
    This rule checks for blank lines before the **else** keyword.

    **Violation**

    .. code-block:: vhdl

        d <= '1';


      else

    **Fix**

    .. code-block:: vhdl

        d <= '1';
      else
    """

    def __init__(self):
        super().__init__(lTokens, iAllow=0, lOverrides=lOverrides)
        self.solution = "Remove blank line(s) before the *else* keyword."
        self.configuration_documentation_link = None
