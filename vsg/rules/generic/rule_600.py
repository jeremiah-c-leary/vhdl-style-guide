# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_suffix_between_tokens_unless_between_tokens as Rule

lTokens = []
lTokens.append(token.interface_constant_declaration.identifier)
lTokens.append(token.interface_signal_declaration.identifier)
lTokens.append(token.interface_variable_declaration.identifier)
lTokens.append(token.interface_unknown_declaration.identifier)

oStart = token.generic_clause.open_parenthesis
oEnd = token.generic_clause.close_parenthesis

lUnless = []
lUnless.append([token.interface_function_specification.function_keyword, token.interface_function_specification.close_parenthesis])
lUnless.append([token.interface_procedure_specification.procedure_keyword, token.interface_procedure_specification.close_parenthesis])


class rule_600(Rule):
    """
    This rule checks for valid suffixes on generic identifiers.
    The default generic suffix is *_g*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       generic(my_generic : integer);

    **Fix**

    .. code-block:: vhdl

       generic(my_generic_g : integer);
    """

    def __init__(self):
        super().__init__(lTokens, oStart, oEnd, lUnless)
        self.suffixes = ["_g"]
