
from vsg import parser
from vsg import token

from vsg.rules import consistent_token_case

lTokens = []
lTokens.append(token.constant_declaration.identifier)

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


class rule_013(consistent_token_case):
    '''
    This rule checks for consistent capitalization of constant names.

    **Violation**

    .. code-block:: vhdl

       architecture RTL of ENTITY1 is

         constant c_size  : integer := 5;
         constant c_ones  : std_logic_vector(c_size - 1 downto 0) := (others => '1');
         constant c_zeros : std_logic_vector(c_size - 1 downto 0) := (others => '0');

         signal data : std_logic_vector(c_size - 1 downto 0);

       begin

         data <= C_ONES;

         PROC_NAME : process () is
         begin

           data <= C_ones;

           if (sig2 = '0') then
             data <= c_Zeros;
           end if;

         end process PROC_NAME;

       end architecture RTL;

    **Fix**

    .. code-block:: vhdl

       architecture RTL of ENTITY1 is

         constant c_size  : integer := 5;
         constant c_ones  : std_logic_vector(c_size - 1 downto 0) := (others => '1');
         constant c_zeros : std_logic_vector(c_size - 1 downto 0) := (others => '0');

         signal data : std_logic_vector(c_size - 1 downto 0);

       begin

         data <= c_ones;

         PROC_NAME : process () is
         begin

           data <= c_ones;

           if (sig2 = '0') then
             data <= c_zeros;
           end if;

         end process PROC_NAME;

       end architecture RTL;
    '''

    def __init__(self):
        consistent_token_case.__init__(self, 'constant', '013', lTokens, lIgnore)
