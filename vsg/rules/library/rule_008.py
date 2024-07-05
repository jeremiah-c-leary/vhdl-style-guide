# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.use_clause.keyword)


class rule_008(token_indent):
    """
    This rule checks the indent of the **use** keyword.

    |configuring_use_clause_indenting_link|

    **Violation**

    .. code-block:: vhdl

       library ieee;
       use ieee.std_logic_1164.all;
            use ieee.std_logic_unsigned.all;

    **Fix**

    .. code-block:: vhdl

       library ieee;
         use ieee.std_logic_1164.all;
         use ieee.std_logic_unsigned.all;
    """

    def __init__(self):
        super().__init__(lTokens)
