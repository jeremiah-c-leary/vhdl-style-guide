# -*- coding: utf-8 -*-

from vsg.rules.whitespace_before_token import Rule
from vsg.token import conditional_waveforms as token


class rule_102(Rule):
    """
    This rule checks for a single space before the **else** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       wr_en <= '0' when (rd_en = '0')else '1';

    **Fix**

    .. code-block:: vhdl

       wr_en <= '0' when (rd_en = '0') else '1';
    """

    def __init__(self):
        super().__init__([token.else_keyword])
