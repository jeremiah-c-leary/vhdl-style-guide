# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.function_specification.close_parenthesis)


class rule_300(token_indent):
    """
    This rule checks the indent of the closing parenthesis if it is on its own line.

    **Violation**

    .. code-block:: vhdl

       function func_1 (a : integer; b : integer;
         c : unsigned(3 downto 0);
         d : std_logic_vector(7 downto 0);
         e : std_logic
         ) return integer is


    **Fix**

    .. code-block:: vhdl

       function func_1 (a : integer; b : integer;
         c : unsigned(3 downto 0);
         d : std_logic_vector(7 downto 0);
         e : std_logic
       ) return integer is
    """

    def __init__(self):
        super().__init__(lTokens)
