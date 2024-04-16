# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import move_token_left_to_next_non_whitespace_token as Rule

lTokens = []
lTokens.append(token.entity_declaration.semicolon)


class rule_025(Rule):
    """
    This rule checks the semicolon is not on its own line.

    **Violation**

    .. code-block:: vhdl

       end entity;

       end entity
       ;

    **Fix**

    .. code-block:: vhdl

       end entity;

       end entity;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.bInsertWhitespace = False
        self.subphase = 3
