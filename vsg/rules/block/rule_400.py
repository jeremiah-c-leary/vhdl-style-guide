# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import align_tokens_in_region_between_tokens_unless_between_tokens

lAlign = []
lAlign.append(token.full_type_declaration.identifier)
lAlign.append(token.incomplete_type_declaration.identifier)
lAlign.append(token.file_declaration.identifier)
lAlign.append(token.constant_declaration.identifier)
lAlign.append(token.signal_declaration.identifier)
lAlign.append(token.subtype_declaration.identifier)
lAlign.append(token.variable_declaration.identifier)
lAlign.append(token.alias_declaration.alias_designator)

lUnless = []
lUnless.append([token.subprogram_body.is_keyword, token.subprogram_body.begin_keyword])


class rule_400(align_tokens_in_region_between_tokens_unless_between_tokens):
    """
    This rule checks the identifiers for all declarations are aligned in the block declarative region.

    |configuring_identifier_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       variable    var1 : natural;
       constant  c_period : time;

    **Fix**

    .. code-block:: vhdl

       variable var1 : natural;
       constant c_period : time;
    """

    def __init__(self):
        super().__init__(lAlign, token.block_statement.block_keyword, token.block_statement.begin_keyword, lUnless)
        self.solution = "Align identifier."
        self.configuration_documentation_link = "configuring_identifier_alignment_rules_link"
        self.configuration.remove("separate_generic_port_alignment")
