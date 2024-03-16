# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import previous_line

lTokens = []
lTokens.append(token.case_generate_statement.generate_label)
lTokens.append(token.for_generate_statement.generate_label)
lTokens.append(token.if_generate_statement.generate_label)


class rule_004(previous_line):
    """
    This rule checks for blank lines or comments before the **generate** label.

    |configuring_previous_line_rules_link|

    **Violation**

    .. code-block:: vhdl

       wr_en <= '1';
       ram_array : for i in 0 to 7 generate

    **Fix**

    .. code-block:: vhdl

       wr_en <= '1';

       ram_array : for i in 0 to 7 generate
    """

    def __init__(self):
        super().__init__(lTokens)
