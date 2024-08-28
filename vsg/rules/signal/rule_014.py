# -*- coding: utf-8 -*-

from vsg import parser, token
from vsg.rules import consistent_token_case as Rule

lTokens = []
lTokens.append(token.signal_declaration.identifier)

lNames = []
lNames.append(parser.todo)
lNames.append(token.todo.name)

lNames.append(token.concurrent_conditional_signal_assignment.target)
lNames.append(token.concurrent_selected_signal_assignment.target)
lNames.append(token.concurrent_simple_signal_assignment.target)

lNames.append(token.conditional_waveform_assignment.target)
lNames.append(token.association_element.actual_part)
lNames.append(token.selected_waveform_assignment.target)
lNames.append(token.selected_force_assignment.target)

lNames.append(token.simple_waveform_assignment.target)
lNames.append(token.simple_force_assignment.target)
lNames.append(token.simple_release_assignment.target)


class rule_014(Rule):
    """
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
           elsif (SiG2 = '1') then
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
           elsif (sig2 = '1') then
             sig1 <= '0';
           end if;

         end process proc_name;

       end architecture rtl;
    """

    def __init__(self):
        super().__init__(lTokens, lNames)
