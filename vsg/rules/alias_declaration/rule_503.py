# -*- coding: utf-8 -*-

from vsg import parser, token
from vsg.rules import consistent_token_case as Rule

lTokens = []
lTokens.append(token.alias_declaration.alias_designator)

lNames = []
lNames.append(parser.todo)


class rule_503(Rule):
    """
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
    """

    def __init__(self):
        super().__init__(lTokens, lNames)
        self.bIncludeDeclarativePartNames = True
