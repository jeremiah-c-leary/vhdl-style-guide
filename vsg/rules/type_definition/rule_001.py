# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.incomplete_type_declaration.type_keyword)
lTokens.append(token.full_type_declaration.type_keyword)


class rule_001(token_indent):
    """
    This rule checks the indent of the **type** declaration.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is

           type state_machine is (idle, write, read, done);

       begin

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is

         type state_machine is (idle, write, read, done);

       begin
    """

    def __init__(self):
        super().__init__(lTokens)
