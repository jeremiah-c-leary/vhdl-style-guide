# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.context_reference.keyword)


class rule_001(token_indent):
    """
    This rule checks the indent of the **context** keyword.

    **Violation**

    .. code-block:: vhdl

       library ieee;
       context c1;

    **Fix**

    .. code-block:: vhdl

       library ieee;
         context c1;
    """

    def __init__(self):
        super().__init__(lTokens)
