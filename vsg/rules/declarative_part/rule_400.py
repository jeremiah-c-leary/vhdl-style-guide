# -*- coding: utf-8 -*-

from vsg import prerequisite, token
from vsg.rules import (
    align_tokens_in_region_between_tokens_unless_between_tokens as Rule,
)

lAlign = []
lAlign.append(token.constant_declaration.assignment_operator)
lAlign.append(token.signal_declaration.assignment_operator)
lAlign.append(token.variable_declaration.assignment_operator)

lUnless = []
lUnless.append([token.subprogram_body.is_keyword, token.subprogram_body.begin_keyword])
lUnless.append([token.protected_type_body.body_keyword, token.protected_type_body.end_keyword])


class rule_400(Rule):
    """
    This rule checks the alignment of **:=** operator for signal, constant and variable declarations.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       signal clk : std_logic := '0';
       variable reset : std_logic := '1';
       shared variable enable : std_logic := '0';
       constant reset_value : integer := 32;

    **Fix**

    .. code-block:: vhdl

       signal clk : std_logic             := '0';
       variable reset : std_logic         := '1';
       shared variable enable : std_logic := '0';
       constant reset_value : integer     := 32;
    """

    def __init__(self):
        super().__init__(lAlign, None, None, lUnless)
        self.solution = "Align :="
        self.prerequisites.append(prerequisite.New("procedure_401"))
        self.prerequisites.append(prerequisite.New("architecture_026"))
        self.subphase = 3
        self.configuration.remove("if_control_statements_ends_group")
        self.configuration.remove("case_control_statements_ends_group")
        self.configuration.remove("loop_control_statements_ends_group")
        self.configuration.remove("separate_generic_port_alignment")

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_in_declarative_parts()
