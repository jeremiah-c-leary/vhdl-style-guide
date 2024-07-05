# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.loop_statement.loop_label)
lTokens.append(token.iteration_scheme.while_keyword)


class rule_300(token_indent):
    """
    This rule checks for indentation of the **while** keyword.
    Proper indentation enhances comprehension.

    **Violation**

    .. code-block:: vhdl

       begin

       while (temp /= 0) loop
           temp := temp/2;
         end loop;

    **Fix**

    .. code-block:: vhdl

       begin

         while (temp /= 0) loop
           temp := temp/2;
         end loop;
    """

    def __init__(self):
        super().__init__(lTokens)
