# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import move_token as Rule

oToken = token.port_clause.close_parenthesis


class rule_014(Rule):
    """
    This rule checks the location of the closing ")" character for the port clause.

    The default location is on a line by itself.

    |configuring_move_token_rules_link|

    **Violation**

    .. code-block:: vhdl

       port (
         WR_EN    : in    std_logic;
         RD_EN    : in    std_logic;
         OVERFLOW : out   std_logic;
         DATA     : inout std_logic);

    **Fix**

    .. code-block:: vhdl

       port (
         WR_EN    : in    std_logic;
         RD_EN    : in    std_logic;
         OVERFLOW : out   std_logic;
         DATA     : inout std_logic
       );
    """

    def __init__(self):
        super().__init__(oToken)
        self.preserve_comment = True
