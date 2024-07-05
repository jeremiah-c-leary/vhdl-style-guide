# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import (
    insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens as Rule,
)

lTokens = []
lTokens.append(token.force_mode.out_keyword)
lTokens.append(token.force_mode.in_keyword)

lTokenPairs = []
lTokenPairs.append([token.selected_force_assignment.with_keyword, token.selected_force_assignment.semicolon])


class rule_007(Rule):
    """
    This rule checks for code after the force mode keywords **in** and **out**.

    **Violation**

    .. code-block:: vhdl

       with mux_sel select addr <= force in "0000" when 0,
         "0001" when 1,
         "1111" when others;

    **Fix**

    .. code-block:: vhdl

       with mux_sel select addr <= force in
         "0000" when 0,
         "0001" when 1,
         "1111" when others;
    """

    def __init__(self):
        super().__init__(lTokens, lTokenPairs)
        self.solution = "Move code after the force mode keyword to the next line."
