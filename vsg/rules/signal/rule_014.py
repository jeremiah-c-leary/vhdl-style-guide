
from vsg import parser
from vsg import token

from vsg.rules import consistent_token_case

lTokens = []
lTokens.append(token.signal_declaration.identifier)

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


class rule_014(consistent_token_case):
    '''
    This rule checks for consistent capitalization of signal names.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of entity1 is

         signal sig1 : std_logic;
         signal sig2 : std_logic;

       begin

         proc_name : process (siG2) is
         begin

           siG1 <= '0';

           if (SIG2 = '0') then
             sIg1 <= '1';
           elisif (SiG2 = '1') then
             SIg1 <= '0';
           end if;

         end process proc_name;

       end architecture rtl;

    **Fix**

    .. code-block:: vhdl

       architecture rtl of entity1 is

         signal sig1 : std_logic;
         signal sig2 : std_logic;

         proc_name : process (sig2) is
         begin

           sig1 <= '0';

           if (sig2 = '0') then
             sig1 <= '1';
           elisif (sig2 = '1') then
             sig1 <= '0';
           end if;

         end process proc_name;

       end architecture rtl;
    '''

    def __init__(self):
        consistent_token_case.__init__(self, 'signal', '014', lTokens, lIgnore)
