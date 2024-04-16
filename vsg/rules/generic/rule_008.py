# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.generic_clause.close_parenthesis)


class rule_008(token_indent):
    """
    This rule checks the indent of the closing parenthesis.

    **Violation**

    .. code-block:: vhdl

       g_depth : integer := 512
       );

    **Fix**

    .. code-block:: vhdl

         g_depth : integer := 512
       );
    """

    def __init__(self):
        super().__init__(lTokens)
