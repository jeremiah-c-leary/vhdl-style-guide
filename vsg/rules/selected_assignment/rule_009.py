# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import (
    insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens as Rule,
)

lTokens = []
lTokens.append(token.delay_mechanism.transport_keyword)
lTokens.append(token.delay_mechanism.inertial_keyword)

lTokenPairs = []
lTokenPairs.append([token.concurrent_selected_signal_assignment.with_keyword, token.concurrent_selected_signal_assignment.semicolon])
lTokenPairs.append([token.selected_waveform_assignment.with_keyword, token.selected_waveform_assignment.semicolon])


class rule_009(Rule):
    """
    This rule checks for code after the delay mechanism keywords **transport** and **inertial**.

    **Violation**

    .. code-block:: vhdl

       with mux_sel select addr <= transport "0000" when 0,
         "0001" when 1,
         "1111" when others;

    **Fix**

    .. code-block:: vhdl

       with mux_sel select addr <= transport
         "0000" when 0,
         "0001" when 1,
         "1111" when others;
    """

    def __init__(self):
        super().__init__(lTokens, lTokenPairs)
        self.solution = "Move code after the delay mechanism keyword to the next line."
