
from vsg import parser
from vsg import token

from vsg.rules import consistent_token_case

lTokens = []
lTokens.append(token.variable_declaration.identifier)

lIgnore = []
lIgnore.append(token.interface_signal_declaration.identifier)
lIgnore.append(token.interface_unknown_declaration.identifier)
lIgnore.append(token.interface_constant_declaration.identifier)
lIgnore.append(token.interface_variable_declaration.identifier)
lIgnore.append(token.association_element.formal_part)
lIgnore.append(token.entity_declaration.identifier)
lIgnore.append(token.entity_declaration.entity_simple_name)
lIgnore.append(token.architecture_body.entity_name)
lIgnore.append(parser.whitespace)
lIgnore.append(parser.carriage_return)
lIgnore.append(parser.blank_line)


class rule_011(consistent_token_case):
    '''
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
           elisif (var2 = '1') then
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
         elisif (var2 = '1') then
           var4 <= '0';
         end if;

       end process proc_name;
    '''

    def __init__(self):
        consistent_token_case.__init__(self, 'variable', '011', lTokens, lIgnore)
