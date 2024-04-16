# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import (
    insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment,
)

lTokens = []
lTokens.append(token.simple_waveform_assignment.semicolon)
lTokens.append(token.simple_force_assignment.semicolon)
lTokens.append(token.simple_release_assignment.semicolon)


class rule_007(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment):
    """
    This rule checks for code after a sequential assignment.

    **Violation**

    .. code-block:: vhdl

        a <= '0'; b <= '1'; c <= '0'; -- comment

    **Fix**

    .. code-block:: vhdl

        a <= '0';
        b <= '1';
        c <= '0'; -- comment
    """

    def __init__(self):
        super().__init__(lTokens)
        self.solution = "Move code after the ; to the next line."
