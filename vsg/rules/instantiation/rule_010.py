# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import align_tokens_in_region_between_tokens

lAlign = []
lAlign.append(token.association_element.assignment)

oStart = token.component_instantiation_statement.label_colon
oEnd = token.component_instantiation_statement.semicolon


class rule_010(align_tokens_in_region_between_tokens):
    """
    This rule checks the alignment of the **=>** operator for each generic and port in the instantiation.

    Following extra configurations are supported:

    * :code:`separate_generic_port_alignment`.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       U_FIFO : FIFO
         generic map (
           g_width => 8,
           g_delay    => 2
         )
         port map (
           wr_en => wr_en,
           rd_en => rd_en,
           overflow => overflow
         );

    **Fix**

    .. code-block:: vhdl

       U_FIFO : FIFO
         generic map (
           g_width => 8,
           g_delay => 2
         )
         port map (
           wr_en    => wr_en,
           rd_en    => rd_en,
           overflow => overflow
         );
    """

    def __init__(self):
        super().__init__(lAlign, oStart, oEnd)
        self.solution = 'Inconsistent alignment of "=>" in generic or port assignments of instantiation.'
        self.configuration.remove("case_control_statements_ends_group")
        self.configuration.remove("if_control_statements_ends_group")
        self.configuration.remove("loop_control_statements_ends_group")
