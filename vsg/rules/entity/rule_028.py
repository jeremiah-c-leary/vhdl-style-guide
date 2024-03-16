# -*- coding: utf-8 -*-

from vsg.rules import (
    insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment as Rule,
)
from vsg.token import entity_declaration as token

lTokens = []
lTokens.append(token.semicolon)


class rule_028(Rule):
    """
    This rule checks for code after the semicolon.

    **Violation**

    .. code-block:: vhdl

       end entity; architecture

    **Fix**

    .. code-block:: vhdl

       end entity;
       architecture
    """

    def __init__(self):
        super().__init__(lTokens)
        self.solution = "Move code after the semicolon to the next line."
