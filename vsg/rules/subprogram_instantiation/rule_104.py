# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.subprogram_instantiation_declaration.new_keyword, token.subprogram_instantiation_declaration.uninstantiated_subprogram_name])


class rule_104(Rule):
    """
    This rule checks for a single space between **new** keyword and the uninstantiated subprogram name.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       procedure my_proc is new     my_generic_proc

    **Fix**

    .. code-block:: vhdl

       procedure my_proc is new my_generic_proc
    """

    def __init__(self):
        super().__init__(lTokens)
