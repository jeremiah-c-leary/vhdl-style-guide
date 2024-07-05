# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.generate_statement_body.begin_keyword)


class rule_006(token_indent):
    """
    This rule checks the indent of the **begin** keyword.

    **Violation**

    .. code-block:: vhdl

       ram_array : for i in 0 to 7 generate
          begin

    **Fix**

    .. code-block:: vhdl

       ram_array : for i in 0 to 7 generate
       begin
    """

    def __init__(self):
        super().__init__(lTokens)
