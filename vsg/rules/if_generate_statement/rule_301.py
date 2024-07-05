# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent as Rule

lTokens = []
lTokens.append(token.if_generate_statement.else_keyword)


class rule_301(Rule):
    """
    This rule checks the indent of the *else* keyword.

    **Violation**

    .. code-block:: vhdl

       ram_array : if condition generate
          else
       end generate;

    **Fix**

    .. code-block:: vhdl

       ram_array : if condition generate
       else
       end generate;
    """

    def __init__(self):
        super().__init__(lTokens)
