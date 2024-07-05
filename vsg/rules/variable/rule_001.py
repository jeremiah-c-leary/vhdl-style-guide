# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.variable_declaration.shared_keyword)
lTokens.append(token.variable_declaration.variable_keyword)


class rule_001(token_indent):
    """
    This rule checks the indent of variable declarations.

    **Violation**

    .. code-block:: vhdl

       proc : process () is

       variable count : integer;
             variable counter : integer;

       begin

    **Fix**

    .. code-block:: vhdl

       proc : process () is

         variable count : integer;
         variable counter : integer;

       begin
    """

    def __init__(self):
        super().__init__(lTokens)
