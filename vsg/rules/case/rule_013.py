# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.null_statement.label)
lTokens.append(token.null_statement.null_keyword)


class rule_013(token_indent):
    """
    This rule checks the indent of the **null** keyword.

    **Violation**

    .. code-block:: vhdl

         when others =>
            null;

         when others =>
       null;

    **Fix**

    .. code-block:: vhdl

       when others =>
         null;

       when others =>
         null;
    """

    def __init__(self):
        super().__init__(lTokens)
