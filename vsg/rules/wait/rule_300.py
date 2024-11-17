# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.wait_statement.label)


class rule_300(token_indent):
    """
    This rule checks for indentation of the label.
    Proper indentation enhances comprehension.

    **Violation**

    .. code-block:: vhdl

       begin

        wait on a,b;
              wait_label : wait until a = '0';

    **Fix**

    .. code-block:: vhdl

       begin

         wait on a,b;
         wait_label : wait until a = '0';
    """

    def __init__(self):
        super().__init__(lTokens)
