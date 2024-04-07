# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_prefix

lTokens = []
lTokens.append(token.constant_declaration.identifier)


class rule_015(token_prefix):
    """
    This rule checks for valid prefixes on constant identifiers.
    The default constant prefix is *c_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       constant my_const : integer;

    **Fix**

    .. code-block:: vhdl

       constant c_my_const : integer;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.prefixes = ["c_"]
