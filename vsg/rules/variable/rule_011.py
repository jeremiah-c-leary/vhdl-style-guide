# -*- coding: utf-8 -*-

from vsg import parser, token
from vsg.rules import consistent_token_case as Rule

lTokens = []
lTokens.append(token.variable_declaration.identifier)

lNames = []
lNames.append(parser.todo)
lNames.append(token.simple_variable_assignment.simple_name)
lNames.append(token.simple_variable_assignment.target)
lNames.append(token.selected_variable_assignment.target)
lNames.append(token.conditional_variable_assignment.target)
lNames.append(token.association_element.actual_part)


class rule_011(Rule):
    """
    This rule checks for consistent capitalization of variable names.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of entity1 is

         shared variable var1 : std_logic;
         shared variable var2 : std_logic;

       begin

         proc_name : process () is

           variable var3 : std_logic;
           variable var4 : std_logic;

         begin

           Var1 <= '0';

           if (VAR2 = '0') then
             vaR3 <= '1';
           elsif (var2 = '1') then
             VAR4 <= '0';
           end if;

         end process proc_name;

       end architecture rtl;

    **Fix**

    .. code-block:: vhdl

       proc_name : process () is

         variable var1 : std_logic;
         variable var2 : std_logic;
         variable var3 : std_logic;
         variable var4 : std_logic;

       begin

         var1 <= '0';

         if (var2 = '0') then
           var3 <= '1';
         elsif (var2 = '1') then
           var4 <= '0';
         end if;

       end process proc_name;
    """

    def __init__(self):
        super().__init__(lTokens, lNames)
