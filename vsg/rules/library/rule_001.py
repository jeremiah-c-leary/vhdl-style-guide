# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.library_clause.keyword)


class rule_001(token_indent):
    """
    This rule checks the indent of the **library** keyword.
    Indenting helps in comprehending the code.


    **Violation**

    .. code-block:: vhdl

       library ieee;
          library fifo_dsn;

    **Fix**

    .. code-block:: vhdl

       library ieee;
       library fifo_dsn;
    """

    def __init__(self):
        super().__init__(lTokens)
