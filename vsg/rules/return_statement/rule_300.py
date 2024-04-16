# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent as Rule

lTokens = []
lTokens.append(token.return_statement.return_keyword)


class rule_300(Rule):
    """
    This rule checks the indentation of the **return** keyword.

    **Violation**

    .. code-block:: vhdl

         return my_value;
         end function;

    **Fix**

    .. code-block:: vhdl

           return my_value;
         end function;
    """

    def __init__(self):
        super().__init__(lTokens)
