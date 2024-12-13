# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_prefix_between_tokens

lTokens = []
lTokens.append(token.identifier.identifier)

oStart = token.package_instantiation_declaration.package_keyword
oEnd = token.package_instantiation_declaration.is_keyword


class rule_601(token_prefix_between_tokens):
    """
    This rule checks for valid prefixes on instantiated package identifiers.
    The default package prefix is *pkg_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       package foo is new my_generic_pkg

    **Fix**

    .. code-block:: vhdl

       package pkg_foo is new my_generic_pkg
    """

    def __init__(self):
        super().__init__(lTokens, oStart, oEnd)
        self.prefixes = ["pkg_"]
