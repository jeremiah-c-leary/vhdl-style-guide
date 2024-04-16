# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import (
    insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens as Rule,
)

lTokens = []
lTokens.append(token.association_list.comma)

lTokenPairs = []
lTokenPairs.append([token.port_map_aspect.open_parenthesis, token.port_map_aspect.close_parenthesis])


class rule_009(Rule):
    """
    This rule checks multiple port assignments on the same line.

    **Violation**

    .. code-block:: vhdl

       port map (
         WR_EN => w_wr_en, RD_EN => w_rd_en,
         OVERFLOW => w_overflow
       );

    **Fix**

    .. code-block:: vhdl

       port map (
         WR_EN => w_wr_en,
         RD_EN => w_rd_en,
         OVERFLOW => w_overflow
       );
    """

    def __init__(self):
        super().__init__(lTokens, lTokenPairs)
        self.solution = "Move multiple port assignments to their own lines."
