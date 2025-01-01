# -*- coding: utf-8 -*-

from vsg.rules import move_token_next_to_another_token
from vsg.token import port_map_aspect as token


class rule_003(move_token_next_to_another_token):
    """
    This rule checks the "(" character is on the same line as the **map** keyword.

    **Violation**

    .. code-block:: vhdl

       port map
       (
         WR_EN    => WR_EN,
         RD_EN    => RD_EN,
         OVERFLOW => OVERFLOW
       );

    **Fix**

    Use explicit port mapping.

    .. code-block:: vhdl

       port map (

         WR_EN    => WR_EN,
         RD_EN    => RD_EN,
         OVERFLOW => OVERFLOW
       );
    """

    def __init__(self):
        super().__init__(token.map_keyword, token.open_parenthesis)
        self.solution = "Move the ( to the same line as the *map* keyword."
        self.subphase = 3
