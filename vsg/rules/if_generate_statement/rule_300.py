# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent as Rule

lTokens = []
lTokens.append(token.if_generate_statement.elsif_keyword)


class rule_300(Rule):
    """
    This rule checks the indent of the **elsif** keyword.

    **Violation**

    .. code-block:: vhdl

       ram_array : if condition generate
          elsif condition generate
       end generate;

    **Fix**

    .. code-block:: vhdl

       ram_array : if condition generate
       elsif condition generate
       end generate;
    """

    def __init__(self):
        super().__init__(lTokens)
