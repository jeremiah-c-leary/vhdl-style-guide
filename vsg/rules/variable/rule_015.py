# -*- coding: utf-8 -*-

from vsg.rules import separate_multiple_variable_identifiers_into_individual_statements

iAllow = 2


class rule_015(separate_multiple_variable_identifiers_into_individual_statements):
    """
    This rule checks for multiple (shared) variable names defined in a single (shared) variable declaration.
    By default, this rule will only flag more than two (shared) variable declarations.

    |configuring_number_of_variables_in_variable_declaration_link|

    **Violation**

    .. code-block:: vhdl

       variable var1, var2
         var3, var4,
         var5
         : std_logic;

       shared variable var6, var7, var8 : std_logic;

    **Fix**

    .. code-block:: vhdl

       variable var1 : std_logic;
       variable var2 : std_logic;
       variable var3 : std_logic;
       variable var4 : std_logic;
       variable var5 : std_logic;

       shared variable var6 : std_logic;
       shared variable var7 : std_logic;
       shared variable var8 : std_logic;
    """

    def __init__(self):
        super().__init__(iAllow)
