# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import blank_line_below_line_ending_with_token

lTokens = []
lTokens.append(token.incomplete_type_declaration.semicolon)
lTokens.append(token.full_type_declaration.semicolon)


class rule_011(blank_line_below_line_ending_with_token):
    """
    This rule checks for a blank line below the **type** declaration.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       type state_machine is (idle, write, read, done);
       signal sm : state_machine;

    **Fix**

    .. code-block:: vhdl

       type state_machine is (idle, write, read, done);

       signal sm : state_machine;
    """

    def __init__(self):
        super().__init__(lTokens)
