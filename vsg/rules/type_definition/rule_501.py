# -*- coding: utf-8 -*-

from vsg import parser, token
from vsg.rules import consistent_token_case as Rule

lTokens = []
lTokens.append(token.enumeration_type_definition.enumeration_literal)

lNames = []
lNames.append(parser.todo)


class rule_501(Rule):
    """
    This rule checks for consistent capitalization of enumerated types.

    **Violation**

    .. code-block:: vhdl

       type state is (IDLE, WRITE, READ);

       state <= Idle;
       state <= write;
       state <= ReAd;

    **Fix**

    .. code-block:: vhdl

       type state is (IDLE, WRITE, READ);

       state <= IDLE;
       state <= WRITE;
       state <= READ;
    """

    def __init__(self):
        super().__init__(lTokens, lNames)
        self.subphase = 2
        self.bIncludeDeclarativePartNames = True
