# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.subprogram_kind.function_keyword, token.subprogram_instantiation_declaration.identifier])


class rule_101(Rule):
    """
    This rule checks for a single space between the **function** keyword and the new subprogram identifier.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       function       my_func is new my_generic_func

    **Fix**

    .. code-block:: vhdl

       function my_func is new my_generic_func
    """

    def __init__(self):
        super().__init__(lTokens)
