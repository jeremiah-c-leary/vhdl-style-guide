# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case as Rule

lTokens = []
lTokens.append(token.selected_waveforms.when_keyword)
lTokens.append(token.selected_expressions.when_keyword)


class rule_503(Rule):
    """
    This rule checks the **when** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       with mux_sel select addr <=
         "0000" WHEN 0,
         "0001" WHEN 1,
         "1111" WHEN others;

    **Fix**

    .. code-block:: vhdl

       with mux_sel select addr <=
         "0000" when 0,
         "0001" when 1,
         "1111" when others;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
