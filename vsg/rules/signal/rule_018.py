# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import move_token_left_to_next_non_whitespace_token as Rule

lTokens = []
lTokens.append(token.signal_declaration.assignment_operator)


class rule_018(Rule):
    """
    This rule checks the **:=** is on the same line as the **signal** keyword.

    **Violation**

    .. code-block:: vhdl

       signal size : integer
          := 1;
       signal width : integer
          := 32;

    **Fix**

    .. code-block:: vhdl

       signal size    : integer :=
         1;
       signal width   : integer :=
         32;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.bRemoveTrailingWhitespace = False
        self.solution = "Move := operator"
