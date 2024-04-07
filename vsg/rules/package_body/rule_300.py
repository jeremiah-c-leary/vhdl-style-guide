# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.package_body.package_keyword)


class rule_300(token_indent):
    """
    This rule checks the indent of the package body keyword.

    **Violation**

    .. code-block:: vhdl

       library ieee;

         package body FIFO_PKG is

    **Fix**

    .. code-block:: vhdl

       library ieee;

       package body FIFO_PKG is
    """

    def __init__(self):
        super().__init__(lTokens)
