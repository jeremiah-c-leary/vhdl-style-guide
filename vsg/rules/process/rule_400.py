# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import align_tokens_in_region_between_tokens_unless_between_tokens

lAlign = []
lAlign.append(token.simple_waveform_assignment.assignment)
lAlign.append(token.simple_force_assignment.assignment)
lAlign.append(token.simple_release_assignment.assignment)
lAlign.append(token.simple_variable_assignment.assignment)
lAlign.append(token.conditional_variable_assignment.assignment)
lAlign.append(token.conditional_waveform_assignment.assignment)

oStart = token.process_statement.begin_keyword
oEnd = token.process_statement.end_keyword

lUnless = []


class rule_400(align_tokens_in_region_between_tokens_unless_between_tokens):
    """
    This rule checks the alignment of the **<=** and **:=** operators over consecutive sequential assignments in the process_statement_part.

    Following extra configurations are supported:

    * :code:`if_control_statements_ends_group`,
    * :code:`case_control_statements_ends_group`.
    * :code:`case_keyword_statements_ends_group`.
    * :code:`loop_control_statements_ends_group`,

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       wr_en <= '1';
       rd_en   <= '0';
       v_variable := 10;

    **Fix**

    .. code-block:: vhdl

       wr_en      <= '1';
       rd_en      <= '0';
       v_variable := 10;
    """

    def __init__(self):
        super().__init__(lAlign, oStart, oEnd, lUnless)
        self.solution = "Align identifier."
        self.if_control_statements_ends_group = "yes"
        self.case_control_statements_ends_group = "yes"
        self.case_keyword_statements_ends_group = "yes"
        self.loop_control_statements_ends_group = "yes"
        self.configuration.remove("separate_generic_port_alignment")
