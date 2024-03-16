# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import align_tokens_in_region_between_tokens as Rule

lAlign = []
lAlign.append(token.element_association.assignment)

oStart = token.concurrent_simple_signal_assignment.assignment
oEnd = token.concurrent_simple_signal_assignment.semicolon


class rule_400(Rule):
    """
    This rule checks the alignment the => operator in record aggregates.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       interface <= (
                     write_words => 12,
                     read_words => 32
                     address => 57
                    );

    **Fix**

    .. code-block:: vhdl

       interface <= (
                     write_words => 12,
                     read_words  => 32
                     address     => 57
                    );
    """

    def __init__(self):
        super().__init__(lAlign, oStart, oEnd)
        self.phase = 5
        self.subphase = 3
        self.solution = "Align =>"
        self.separate_generic_port_alignment = "no"
        self.comment_line_ends_group = "no"
        self.blank_line_ends_group = "no"
        self.configuration.remove("separate_generic_port_alignment")
        self.configuration.remove("case_control_statements_ends_group")
        self.configuration.remove("if_control_statements_ends_group")
        self.configuration.remove("loop_control_statements_ends_group")
        self.bIncludeTillBeginningOfLine = True
        self.configuration.append("aggregate_parens_ends_group")
        self.configuration.append("ignore_single_line_aggregates")
