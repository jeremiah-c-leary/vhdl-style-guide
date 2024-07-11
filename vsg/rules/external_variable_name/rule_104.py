# -*- coding: utf-8 -*-

from vsg.rules.whitespace_before_token import Rule
from vsg.token import external_variable_name as token


class rule_104(Rule):
    """
    This rule checks for a single space before the double greater than.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       << variable dut.fifo.wr_en : std_logic>>
       << variable dut.fifo.wr_en : std_logic     >>

    **Fix**

    .. code-block:: vhdl

       << variable dut.fifo.wr_en : std_logic >>
       << variable dut.fifo.wr_en : std_logic >>
    """

    def __init__(self):
        Rule.__init__(self, [token.double_greater_than])
