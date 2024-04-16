# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.context_declaration.end_keyword)


class rule_020(token_indent):
    """
    This rule checks the indent of the **end** keyword.

    **Violation**

    .. code-block:: vhdl

       context c1 is
          end context c1;

    **Fix**

    .. code-block:: vhdl

       context c1 is
       end context c1;
    """

    def __init__(self):
        super().__init__(lTokens)
