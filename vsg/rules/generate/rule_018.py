# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.generate_statement_body.end_keyword)


class rule_018(token_indent):
    """
    This rule checks the indent of the **end** keyword in the generate statement body.

    **Violation**

    .. code-block:: vhdl

       ram_array : for i in 0 to 7 generate
       begin
         end;
       end generate;

    **Fix**

    .. code-block:: vhdl

       ram_array : for i in 0 to 7 generate
       begin
       end;
       end generate;
    """

    def __init__(self):
        super().__init__(lTokens)
