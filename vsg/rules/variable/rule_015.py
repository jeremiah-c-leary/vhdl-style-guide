# -*- coding: utf-8 -*-

from vsg.rules import separate_multiple_variable_identifiers_into_individual_statements

iAllow = 2


class rule_015(separate_multiple_variable_identifiers_into_individual_statements):
    """
    This rule checks for multiple variable names defined in a single variable declaration.
    By default, this rule will only flag more than two variable declarations.

    |configuring_number_of_variables_in_variable_declaration_link|

    **Violation**

    .. code-block:: vhdl

       variable sig1, sig2
         sig3, sig4,
         sig5
         : std_logic;

    **Fix**

    .. code-block:: vhdl

       variable sig1 : std_logic;
       variable sig2 : std_logic;
       variable sig3 : std_logic;
       variable sig4 : std_logic;
       variable sig5 : std_logic;
    """

    def __init__(self):
        super().__init__(iAllow)
