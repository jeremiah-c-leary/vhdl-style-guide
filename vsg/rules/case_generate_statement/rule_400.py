# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import align_tokens_in_region_between_tokens as Rule

lAlign = []
lAlign.append(token.case_generate_alternative.assignment)

oStart = token.case_generate_statement.case_keyword
oEnd = token.case_generate_statement.end_keyword


class rule_400(Rule):
    """
    This rule checks the *=>* are aligned in case_generate_alternatives.

    .. NOTE:: The default configuration is :code:`compact_alignment`.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       gc : case I generate
         when 1 =>
         when n_order =>
         when others =>
       end generate gc;

    **Fix**

    .. code-block:: vhdl

       gc : case I generate
         when 1       =>
         when n_order =>
         when others  =>
       end generate gc;
    """

    def __init__(self):
        super().__init__(lAlign, oStart, oEnd)
        self.solution = 'Inconsistent alignment of "=>".'
        self.disable = True
        self.compact_alignment = "yes"
        self.blank_line_ends_group = "no"
        self.comment_line_ends_group = "no"
        self.separate_generic_port_alignment = "no"
        self.configuration.remove("separate_generic_port_alignment")
        self.configuration.remove("case_control_statements_ends_group")
        self.configuration.remove("if_control_statements_ends_group")
        self.configuration.remove("loop_control_statements_ends_group")
