# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_suffix_between_tokens

lTokens = []
lTokens.append(token.interface_constant_declaration.identifier)
lTokens.append(token.interface_signal_declaration.identifier)
lTokens.append(token.interface_variable_declaration.identifier)
lTokens.append(token.interface_unknown_declaration.identifier)


class rule_600(token_suffix_between_tokens):
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
        super().__init__(lTokens, token.generic_clause.open_parenthesis, token.generic_clause.close_parenthesis)
        self.suffixes = ["_g"]
