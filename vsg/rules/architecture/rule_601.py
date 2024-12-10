# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import consistent_interface_token_case


class rule_601(consistent_interface_token_case.consistent_interface_token_case):
    """
    This rule checks for consistent capitalization of port names in an architecture body.

    **Violation**

    .. code-block:: vhdl

       entity FIFO is
         port (
           I_DATA : in std_logic_vector(31 downto 0)
         );
       end entity fifo;

       architecture rtl of fifo is

       begin

          register <= i_data;

       end architecture rtl;

    **Fix**

    .. code-block:: vhdl

       entity FIFO is
         port (
           I_DATA : in std_logic_vector(31 downto 0)
         );
       end entity fifo;

       architecture rtl of fifo is

       begin

          register <= I_DATA;

       end architecture rtl;
    """

    def __init__(self):
        super().__init__()
        self.clause_token = token.port_clause
        self.interface_string = "Port"
        self.map_aspect_token = token.port_map_aspect
