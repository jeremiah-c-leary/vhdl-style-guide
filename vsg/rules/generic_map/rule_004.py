# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import move_token as Rule

oToken = token.generic_map_aspect.close_parenthesis


class rule_004(Rule):
    """
    This rule checks the location of the closing ")" character for the generic map.

    The default location is on a line by itself.

    |configuring_move_token_rules_link|

    **Violation**

    .. code-block:: vhdl

         generic map (
           GENERIC_1 => 0,
           GENERIC_2 => TRUE,
           GENERIC_3 => FALSE)

    **Fix**

    .. code-block:: vhdl

         generic map (
           GENERIC_1 => 0,
           GENERIC_2 => TRUE,
           GENERIC_3 => FALSE
         )
    """

    def __init__(self):
        super().__init__(oToken)
