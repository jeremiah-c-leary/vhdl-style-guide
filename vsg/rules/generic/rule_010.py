# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import move_token as Rule

oToken = token.generic_clause.close_parenthesis


class rule_010(Rule):
    """
    This rule checks the location of the closing ")" character for the generic clause.

    The default location is on a line by itself.

    |configuring_move_token_rules_link|

    **Violation**

    .. code-block:: vhdl

       g_depth : integer := 512);

    **Fix**

    .. code-block:: vhdl

         g_depth : integer := 512
       );
    """

    def __init__(self):
        super().__init__(oToken)
        self.preserve_comment = True
