# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import remove_carriage_return_after_token as Rule

lTokens = []
lTokens.append(token.selected_expressions.when_keyword)
lTokens.append(token.selected_waveforms.when_keyword)


class rule_011(Rule):
    """
    This rule checks the choice is on the same line as the **when** keyword.

    **Violation**

    .. code-block:: vhdl

       with
         mux_sel select addr <=
         "0000" when
         0,
         "0001" when 1,
         "1111" when others;

    **Fix**

    .. code-block:: vhdl

       with mux_sel select addr <=
         "0000" when 0,
         "0001" when 1,
         "1111" when others;
    """

    def __init__(self):
        super().__init__(lTokens, bInsertSpace=True)
        self.solution = "Removed carraige returns after when keyword"
