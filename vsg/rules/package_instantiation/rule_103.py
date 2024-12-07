# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.package_instantiation_declaration.new_keyword, token.package_instantiation_declaration.uninstantiated_package_name])


class rule_103(Rule):
    """
    This rule checks for a single space between **new** keyword and the uninstantiated package name.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       package my_pkg is new    my_generic_pkg

    **Fix**

    .. code-block:: vhdl

       package my_pkg is new my_generic_pkg
    """

    def __init__(self):
        super().__init__(lTokens)
