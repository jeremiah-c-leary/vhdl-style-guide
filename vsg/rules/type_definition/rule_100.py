# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_between_token_pairs import Rule

lTokenPairs = []
lTokenPairs.append([token.full_type_declaration.type_keyword, token.full_type_declaration.identifier])
lTokenPairs.append([token.incomplete_type_declaration.type_keyword, token.incomplete_type_declaration.identifier])


class rule_100(Rule):
    """
    This rule checks for a single space before the identifier.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       type          t_my_type is range -5 to 5;

    **Fix**

    .. code-block:: vhdl

       type t_my_type is range -5 to 5;
    """

    def __init__(self):
        super().__init__(lTokenPairs)
        self.disable = True
