
from vsg import parser
from vsg import token

from vsg.rules import consistent_token_case as Rule

lTokens = []
lTokens.append(token.alias_declaration.alias_designator)

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


class rule_503(Rule):
    '''
    This rule checks for consistent capitalization of alias designators.

    **Violation**

    .. code-block:: vhdl

       architecture RTL of ENTITY1 is

         signal instructure : bit_vector(15 downto 0);
         alias opcode : bit_vector(3 downto 0) is instructure(15 downto 12);

         signal data : std_logic_vector(OPCODE'range);

       begin

         data <= OpCode;

         PROC_NAME : process () is
         begin

           data <= OpCOde;

           if (opCODE = "0110") then
             data <= oPCode;
           end if;

         end process PROC_NAME;

       end architecture RTL;

    **Fix**

    .. code-block:: vhdl

       architecture RTL of ENTITY1 is

         signal instructure : bit_vector(15 downto 0);
         alias opcode : bit_vector(3 downto 0) is instructure(15 downto 12);

         signal data : std_logic_vector(opcode'range);

       begin

         data <= opcode;

         PROC_NAME : process () is
         begin

           data <= opcode;

           if (opcode = "0110") then
             data <= opcode;
           end if;

         end process PROC_NAME;

       end architecture RTL;
    '''

    def __init__(self):
        Rule.__init__(self, 'alias_declaration', '503', lTokens, lIgnore)
