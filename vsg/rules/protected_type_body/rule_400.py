# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import (
    align_tokens_in_region_between_tokens_unless_between_tokens as Rule,
)

lAlign = []
lAlign.append(token.full_type_declaration.identifier)
lAlign.append(token.incomplete_type_declaration.identifier)
lAlign.append(token.file_declaration.identifier)
lAlign.append(token.constant_declaration.identifier)
lAlign.append(token.subtype_declaration.identifier)
lAlign.append(token.variable_declaration.identifier)
lAlign.append(token.alias_declaration.alias_designator)

oStart = token.protected_type_body.body_keyword
oEnd = token.protected_type_body.end_body_keyword

lUnless = []
lUnless.append([token.subprogram_body.is_keyword, token.subprogram_body.begin_keyword])


class rule_400(Rule):
    """
    This rule checks the identifiers for all declarations are aligned in the protected type body declarative region.

    |configuring_identifier_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       variable    var1 : natural;
       constant  c_period : time;

    **Fix**

    .. code-block:: vhdl

       variable var1     : natural;
       constant c_period : time;
    """

    def __init__(self):
        super().__init__(lAlign, oStart, oEnd, lUnless)
        self.solution = "Align identifier."
        self.configuration_documentation_link = "configuring_identifier_alignment_rules_link"
        self.configuration.remove("separate_generic_port_alignment")
        self.configuration.remove("if_control_statements_ends_group")
        self.configuration.remove("case_control_statements_ends_group")
        self.configuration.remove("loop_control_statements_ends_group")
