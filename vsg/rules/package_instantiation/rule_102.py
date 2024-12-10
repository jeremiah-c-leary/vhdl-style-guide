# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.package_instantiation_declaration.is_keyword, token.package_instantiation_declaration.new_keyword])


class rule_102(Rule):
    """
    This rule checks for a single space between the **is** keyword and the **new** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       package my_pkg is    new my_generic_pkg

    **Fix**

    .. code-block:: vhdl

       package my_pkg is new my_generic_pkg
    """

    def __init__(self):
        super().__init__(lTokens)
