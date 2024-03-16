# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.enumeration_type_definition.close_parenthesis)


class rule_016(token_indent):
    """
    This rule checks the indent of the closing parenthesis on multiline types.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is

         type state_machine is (
           idle, write, read, done
           );

       begin

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is

         type state_machine is (
           idle, write, read, done
         );

       begin
    """

    def __init__(self):
        super().__init__(lTokens)
