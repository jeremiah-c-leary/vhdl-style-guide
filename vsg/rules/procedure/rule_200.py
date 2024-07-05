# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import previous_line

lTokens = []
lTokens.append(token.procedure_specification.procedure_keyword)


class rule_200(previous_line):
    """
    This rule checks for blank lines or comments above the **procedure** keyword.

    |configuring_previous_line_rules_link|

    **Violation**

    .. code-block:: vhdl

       architecture RTL of FIFO is
         procedure proc1 is


    **Fix**

    .. code-block:: vhdl

       architecture RTL of FIFO is

         procedure proc1 is
    """

    def __init__(self):
        super().__init__(lTokens)
