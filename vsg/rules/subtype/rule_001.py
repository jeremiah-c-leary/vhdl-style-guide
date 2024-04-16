# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.subtype_declaration.subtype_keyword)


class rule_001(token_indent):
    """
    This rule checks for indentation of the **subtype** keyword.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is

            subtype read_size is range 0 to 9;
       subtype write_size is range 0 to 9;

       begin

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is

         subtype read_size is range 0 to 9;
         subtype write_size is range 0 to 9;

       begin

    """

    def __init__(self):
        super().__init__(lTokens)
