# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.package_declaration.end_keyword)


class rule_015(token_indent):
    """
    This rule checks the indent of the end package declaration.

    **Violation**

    .. code-block:: vhdl

       package FIFO_PKG is

          end package fifo_pkg;

    **Fix**

    .. code-block:: vhdl

       package fifo_pkg is

       end package fifo_pkg;
    """

    def __init__(self):
        super().__init__(lTokens)
