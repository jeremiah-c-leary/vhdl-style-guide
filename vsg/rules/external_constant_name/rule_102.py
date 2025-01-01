# -*- coding: utf-8 -*-

from vsg.rules.whitespace_before_token import Rule
from vsg.token import external_constant_name as token


class rule_102(Rule):
    """
    This rule checks for a single space before the colon.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       << constant dut.fifo.wr_en: std_logic >>
       << constant dut.fifo.wr_en        : std_logic >>

    **Fix**

    .. code-block:: vhdl

       << constant dut.fifo.wr_en : std_logic >>
       << constant dut.fifo.wr_en : std_logic >>
    """

    def __init__(self):
        Rule.__init__(self, [token.colon])
