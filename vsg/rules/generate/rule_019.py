# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import split_line_at_token

lTokens = []
lTokens.append(token.case_generate_statement.end_keyword)
lTokens.append(token.for_generate_statement.end_keyword)
lTokens.append(token.if_generate_statement.end_keyword)


class rule_019(split_line_at_token):
    """
    This rule checks the **end** keyword is on its own line.

    **Violation**

    .. code-block:: vhdl

       ram_array : for i in 0 to 7 generate
        a <= b; end generate;

    **Fix**

    .. code-block:: vhdl

       ram_array : for i in 0 to 7 generate
         a <= b;
       end generate;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.solution = "Move end keyword and any code after it to the next line"
