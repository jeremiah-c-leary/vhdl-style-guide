# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_suffix_between_tokens

lTokens = []
lTokens.append(token.identifier.identifier)

oStart = token.package_instantiation_declaration.package_keyword
oEnd = token.package_instantiation_declaration.is_keyword


class rule_600(token_suffix_between_tokens):
    """
    This rule checks for valid suffixes on package identifiers.
    The default package suffix is *_pkg*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       package foo is new my_generic_pkg

    **Fix**

    .. code-block:: vhdl

       package foo_pkg is new my_generic_pkg
    """

    def __init__(self):
        super().__init__(lTokens, oStart, oEnd)
        self.suffixes = ["_pkg"]
