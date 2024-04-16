# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import align_tokens_in_region_between_tokens

lAlign = []
lAlign.append(token.interface_unknown_declaration.colon)


class rule_017(align_tokens_in_region_between_tokens):
    """
    This rule checks the alignment of the colon for each generic and port in the entity declaration.

    Following extra configurations are supported:

    * :code:`separate_generic_port_alignment`.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       generic (
           g_width : positive;
           g_output_delay : positive
       );
       port (
           clk_i : in std_logic;
           data_i : in std_logic;
           data_o : in std_logic
       );

    **Fix**

    .. code-block:: vhdl

       generic (
           g_width        : positive;
           g_output_delay : positive
       );
       port (
           clk_i  : in std_logic;
           data_i : in std_logic;
           data_o : in std_logic
       );
    """

    def __init__(self):
        super().__init__(lAlign, token.entity_declaration.entity_keyword, token.entity_declaration.end_keyword)
        self.solution = "Align :."
        self.configuration.remove("case_control_statements_ends_group")
        self.configuration.remove("if_control_statements_ends_group")
        self.configuration.remove("loop_control_statements_ends_group")
