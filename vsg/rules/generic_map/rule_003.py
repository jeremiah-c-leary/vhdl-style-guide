# -*- coding: utf-8 -*-

from vsg.rules import move_token_next_to_another_token
from vsg.token import generic_map_aspect as token


class rule_003(move_token_next_to_another_token):
    """
    This rule checks the ( is on the same line as the **map** keyword.

    **Violation**

    .. code-block:: vhdl

       generic map
       (
         WIDTH => 32,
         DEPTH => 512
       )

    **Fix**

    Use explicit port mapping.

    .. code-block:: vhdl

       generic map (
         WIDTH => 32,
         DEPTH => 512
       )
    """

    def __init__(self):
        super().__init__(token.map_keyword, token.open_parenthesis)
        self.solution = "Move the ( to the same line as the *map* keyword."
        # The subphase must be changed so that this rule runs after the rule to move the map keyword.
        self.subphase = 3
