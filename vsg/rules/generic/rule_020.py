# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_prefix_between_tokens

lTokens = []
lTokens.append(token.interface_constant_declaration.identifier)
lTokens.append(token.interface_signal_declaration.identifier)
lTokens.append(token.interface_variable_declaration.identifier)
lTokens.append(token.interface_unknown_declaration.identifier)


class rule_020(token_prefix_between_tokens):
    """
    This rule checks for valid prefixes on generic identifiers.
    The default generic prefix is *g_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       generic(my_generic : integer);

    **Fix**

    .. code-block:: vhdl

       generic(g_my_generic : integer);
    """

    def __init__(self):
        super().__init__(lTokens, token.generic_clause.open_parenthesis, token.generic_clause.close_parenthesis)
        self.prefixes = ["g_"]
