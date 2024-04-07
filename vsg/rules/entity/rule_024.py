# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import move_token_left_to_next_non_whitespace_token as Rule

lTokens = []
lTokens.append(token.entity_declaration.entity_simple_name)


class rule_024(Rule):
    """
    This rule checks the end entity simple name is not on its own line.

    **Violation**

    .. code-block:: vhdl

       end entity FIFO;

       end entity
         FIFO;

    **Fix**

    .. code-block:: vhdl

       end entity FIFO;

       end entity FIFO;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.subphase = 2
        self.bRemoveTrailingWhitespace = False
