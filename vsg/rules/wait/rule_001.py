# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.wait_statement.wait_keyword)


class rule_001(token_indent):
    """
    This rule checks for indentation of the **wait** keyword.
    Proper indentation enhances comprehension.

    **Violation**

    .. code-block:: vhdl

       begin

           wait for 10ns;
        wait on a,b;
              wait until a = '0';

    **Fix**

    .. code-block:: vhdl

       begin

         wait for 10ns;
         wait on a,b;
         wait until a = '0';
    """

    def __init__(self):
        super().__init__(lTokens)
