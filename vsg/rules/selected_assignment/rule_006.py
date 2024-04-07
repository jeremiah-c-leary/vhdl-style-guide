# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import (
    insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment as Rule,
)

lTokens = []
lTokens.append(token.selected_force_assignment.force_keyword)


class rule_006(Rule):
    """
    This rule checks for code after the **force** keyword.

    **Violation**

    .. code-block:: vhdl

       with mux_sel select addr <= force "0000" when 0,
         "0001" when 1,
         "1111" when others;

    **Fix**

    .. code-block:: vhdl

       with mux_sel select addr <= force
         "0000" when 0,
         "0001" when 1,
         "1111" when others;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.solution = "Move code after the force keyword to the next line."
