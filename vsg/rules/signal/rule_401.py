# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import (
    align_tokens_in_region_between_tokens_unless_between_tokens as Rule,
)

lAlign = []
lAlign.append(token.element_association.assignment)

lUnless = []

oStartToken = token.signal_declaration.assignment_operator
oEndToken = token.signal_declaration.semicolon


class rule_401(Rule):
    """
    This rule checks the alignment of assignment keywords in signal declarations.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       signal c_default_values : t_address_en := (
         c_address_control => false,
         c_address_data => true,
         others => false
       );

    **Fix**

    .. code-block:: vhdl

       signal c_default_values : t_address_en := (
         c_address_control => false,
         c_address_data    => true,
         others            => false
       );
    """

    def __init__(self):
        super().__init__(lAlign, oStartToken, oEndToken, lUnless)
        self.solution = "Align => ."
        self.configuration.remove("if_control_statements_ends_group")
        self.configuration.remove("case_control_statements_ends_group")
        self.configuration.remove("loop_control_statements_ends_group")
        self.configuration.remove("separate_generic_port_alignment")
        self.configuration.append("aggregate_parens_ends_group")
        self.configuration.append("ignore_single_line_aggregates")
