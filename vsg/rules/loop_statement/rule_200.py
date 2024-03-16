# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import previous_line

lTokens = []
lTokens.append(token.loop_statement.loop_label)
lTokens.append(token.iteration_scheme.while_keyword)
lTokens.append(token.iteration_scheme.for_keyword)
lTokens.append(token.loop_statement.loop_keyword)


class rule_200(previous_line):
    """
    This rule checks for blank lines or comments above loop statements.

    |configuring_previous_line_rules_link|

    The default style is :code:`no_code`.

    **Violation**

    .. code-block:: vhdl

       -- Comment
       LOOP_LABEL : loop

       wr_en <= wr_en;
       LOOP_LABEL : loop

    **Fix**

    .. code-block:: vhdl

       -- Comment
       LOOP_LABEL : loop

       wr_en <= wr_en;

       LOOP_LABEL : loop
    """

    def __init__(self):
        super().__init__(lTokens)
        self.style = "no_code"
