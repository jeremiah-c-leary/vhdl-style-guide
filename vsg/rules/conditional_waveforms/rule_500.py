# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case as Rule

lTokens = []
lTokens.append(token.conditional_waveforms.when_keyword)


class rule_500(Rule):
    """
    This rule checks the **when** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       wr_en <= '0' WHEN (rd_en = '0') else '1';

    **Fix**

    .. code-block:: vhdl

       wr_en <= '0' when (rd_en = '0') else '1';
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
