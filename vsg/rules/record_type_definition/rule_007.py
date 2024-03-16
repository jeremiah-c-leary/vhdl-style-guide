# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import move_token_left_to_next_non_whitespace_token as Rule

lTokens = []
lTokens.append(token.full_type_declaration.semicolon)


class rule_007(Rule):
    """
    This rule checks the semicolon is on the same line as the **record** keyword.

    **Violation**

    .. code-block:: vhdl

       type t_record is record
         a : std_logic;
         b : std_logic;
       end record t_record
       ;

    **Fix**

    .. code-block:: vhdl

       type t_record is record
         a : std_logic;
         b : std_logic;
       end record t_record;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.bInsertWhitespace = False
        self.subphase = 3
