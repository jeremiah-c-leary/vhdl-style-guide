# -*- coding: utf-8 -*-

from vsg.rules import move_token_next_to_another_token
from vsg.token import generic_map_aspect as token


class rule_009(move_token_next_to_another_token):
    """
    This rule checks the **map** keyword is on the same line as the **generic** keyword.

    **Violation**

    .. code-block:: vhdl

       generic
       map (
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
        super().__init__(token.generic_keyword, token.map_keyword)
        self.solution = "Move the *map* keyword to the same line as the *generic* keyword."
