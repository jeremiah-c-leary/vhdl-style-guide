# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_suffix

lTokens = []
lTokens.append(token.variable_declaration.identifier)


class rule_600(token_suffix):
    """
    This rule checks for valid suffix on variable identifiers.
    The default variable suffix is *_v*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       variable my_var : natural;

    **Fix**

    .. code-block:: vhdl

       variable my_var_v : natural;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.suffixes = ["_v"]
        self.solution = "Variable identifiers"
