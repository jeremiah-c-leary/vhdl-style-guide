# -*- coding: utf-8 -*-

from vsg.rules import move_token_next_to_another_token
from vsg.token import port_map_aspect as token


class rule_011(move_token_next_to_another_token):
    """
    This rule checks the **map** keyword is on the same line as the **port** keyword.

    **Violation**

    .. code-block:: vhdl

       port
       map (
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
        super().__init__(token.port_keyword, token.map_keyword)
        # The subphase must be changed so that this rule runs after the rule to move the map keyword.
        self.solution = "Move the *port* keyword to the same line as the *map* keyword."
