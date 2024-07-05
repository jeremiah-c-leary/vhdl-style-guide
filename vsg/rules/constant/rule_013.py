# -*- coding: utf-8 -*-

from vsg import parser, token
from vsg.rules import consistent_token_case as Rule

lTokens = []
lTokens.append(token.constant_declaration.identifier)

lNames = []
lNames.append(parser.todo)


class rule_013(Rule):
    """
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
    """

    def __init__(self):
        super().__init__(lTokens, lNames)
        self.bIncludeDeclarativePartNames = True
