# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import move_token_left_to_next_non_whitespace_token as Rule

lTokens = []
lTokens.append(token.constant_declaration.assignment_operator)


class rule_007(Rule):
    """
    This rule checks the **:=** is on the same line at the **constant** keyword.

    **Violation**

    .. code-block:: vhdl

       constant size : integer
          := 1;
       constant width : integer
          := 32;

    **Fix**

    .. code-block:: vhdl

       constant size    : integer :=
         1;
       constant width   : integer :=
         32
    """

    def __init__(self):
        super().__init__(lTokens)
        self.bRemoveTrailingWhitespace = False
