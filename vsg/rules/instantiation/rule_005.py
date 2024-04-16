# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import split_line_at_token_when_between_tokens

lTokens = []
lTokens.append(token.port_map_aspect.port_keyword)

oStart = token.component_instantiation_statement.label_colon
oEnd = token.component_instantiation_statement.semicolon


class rule_005(split_line_at_token_when_between_tokens):
    """
    This rule checks the **port map** keywords are on their own line.

    **Violation**

    .. code-block:: vhdl

       U_FIFO : FIFO port map (

    **Fix**

    .. code-block:: vhdl

       U_FIFO : FIFO
         port map (
    """

    def __init__(self):
        super().__init__(lTokens, oStart, oEnd)
        self.solution = "Place *port map* keywords on the next line by itself"
