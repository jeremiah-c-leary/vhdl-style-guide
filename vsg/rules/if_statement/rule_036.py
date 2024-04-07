# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import move_token_left_to_next_non_whitespace_token as Rule

lTokens = []
lTokens.append(token.if_statement.then_keyword)


class rule_036(Rule):
    """
    This rule checks the **then** keyword is not on a line by itself.

    **Violation**

    .. code-block:: vhdl

       if a = '1'
         then

    **Fix**

    .. code-block:: vhdl

       if a = '1' then
    """

    def __init__(self):
        super().__init__(lTokens)
