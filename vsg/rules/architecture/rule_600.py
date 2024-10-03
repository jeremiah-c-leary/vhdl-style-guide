# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.consistent_interface_token_case import consistent_interface_token_case as Rule


class rule_600(Rule):
    """
    This rule checks for consistent capitalization of generic names in an architecture body.

    **Violation**

    .. code-block:: vhdl

       entity FIFO is
         generic (
           G_WIDTH : natural := 16
         );
       end entity fifo;

       architecture rtl of fifo is

          signal w_data : std_logic_vector(g_width - 1 downto 0);

       begin

          output <= large_data(g_width - 1 downto 0);

       end architecture rtl;

    **Fix**

    .. code-block:: vhdl

       entity FIFO is
         generic (
           G_WIDTH : natural := 16
         );
       end entity fifo;

       architecture rtl of fifo is

          signal w_data : std_logic_vector(G_WIDTH - 1 downto 0);

       begin

          output <= large_data(G_WIDTH - 1 downto 0);

       end architecture rtl;
    """

    def __init__(self):
        super().__init__()
        self.map_aspect_token = token.generic_map_aspect
        self.clause_token = token.generic_clause
