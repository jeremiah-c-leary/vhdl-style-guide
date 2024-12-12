# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import (
    token_case_in_range_bounded_by_tokens_unless_between_tokens as Rule,
)

lTokens = []
lTokens.append(token.interface_constant_declaration.identifier)
lTokens.append(token.interface_signal_declaration.identifier)
lTokens.append(token.interface_variable_declaration.identifier)
lTokens.append(token.interface_file_declaration.identifier)
lTokens.append(token.interface_unknown_declaration.identifier)

oStart = token.generic_clause.open_parenthesis
oEnd = token.generic_clause.close_parenthesis

lUnless = []
lUnless.append([token.interface_function_specification.function_keyword, token.interface_function_specification.close_parenthesis])
lUnless.append([token.interface_procedure_specification.procedure_keyword, token.interface_procedure_specification.close_parenthesis])


class rule_007(Rule):
    """
    This rule checks the generic names have proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       G_WIDTH : integer := 32;

    **Fix**

    .. code-block:: vhdl

       g_width : integer := 32;
    """

    def __init__(self):
        super().__init__(lTokens, oStart, oEnd, lUnless)
        self.configuration.append("prefix_exceptions")
        self.configuration.append("suffix_exceptions")
        self.configuration.append("case_exceptions")
        self.groups.append("case::name")
