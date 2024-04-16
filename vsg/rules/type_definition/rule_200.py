# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import blank_line_below_line_ending_with_token as Rule

lTokens = []
lTokens.append(token.full_type_declaration.semicolon)
lTokens.append(token.incomplete_type_declaration.semicolon)

lAllowTokens = []
lAllowTokens.append(token.full_type_declaration.type_keyword)
lAllowTokens.append(token.incomplete_type_declaration.type_keyword)


class rule_200(Rule):
    """
    This rule checks for a blank line below a type declaration unless there is another type declaration.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       type state_machine_t is (idle, write, read, done);
       type state_machine is (idle, write, read, done);
       constant width : integer := 32;

    **Fix**

    .. code-block:: vhdl

       type state_machine_t is (idle, write, read, done);
       type state_machine is (idle, write, read, done);

       constant width : integer := 32;
    """

    def __init__(self):
        super().__init__(lTokens, lAllowTokens)
        self.disable = True
        self.configuration.remove("style")
