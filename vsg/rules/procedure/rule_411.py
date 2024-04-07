# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import align_tokens_in_region_between_tokens

lAlign = []
lAlign.append(token.interface_signal_declaration.assignment)
lAlign.append(token.interface_constant_declaration.assignment)
lAlign.append(token.interface_variable_declaration.assignment)
lAlign.append(token.interface_unknown_declaration.assignment)


class rule_411(align_tokens_in_region_between_tokens):
    """
    This rule checks the alignment of **:=** operator for each parameter in the procedure declaration.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

         procedure average_samples (
           constant a : in integer := 0;
           signal d : out std_logic   := 'X';
         );

    **Fix**

    .. code-block:: vhdl

         procedure average_samples (
           constant a : in integer  := 0;
           signal d : out std_logic := 'X';
         );
    """

    def __init__(self):
        align_tokens_in_region_between_tokens.__init__(
            self,
            lAlign,
            token.procedure_specification.open_parenthesis,
            token.procedure_specification.close_parenthesis,
        )
        self.solution = "Align :."
        self.configuration.remove("case_control_statements_ends_group")
        self.configuration.remove("if_control_statements_ends_group")
        self.configuration.remove("loop_control_statements_ends_group")
