# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.subprogram_kind.procedure_keyword, token.subprogram_instantiation_declaration.identifier])


class rule_100(Rule):
    """
    This rule checks for a single space between the **procedure** keyword and the new subprogram identifier.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       procedure       my_proc is new my_generic_proc

    **Fix**

    .. code-block:: vhdl

       procedure my_proc is new my_generic_proc
    """

    def __init__(self):
        super().__init__(lTokens)
