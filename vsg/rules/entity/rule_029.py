# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import split_line_at_token

lTokens = []
lTokens.append(token.entity_declaration.begin_keyword)


class rule_029(split_line_at_token):
    """
    This rule checks the **begin** keyword is on its own line.

    **Violation**

    .. code-block:: vhdl

       entity FIFO is
         port (
           I_INPUT : in std_logic
         ); begin
       end entity;

    **Fix**

    .. code-block:: vhdl

       entity FIFO is
         port (
           I_INPUT : in std_logic
         );
       begin
       end entity;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.solution = "Move the **begin** keyword to the next line."
