# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_before_token import Rule

lTokens = []
lTokens.append(token.unbounded_array_definition.of_keyword)


class rule_101(Rule):
    """
    This rule checks for a single space before the **of** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       type t_u_array_unconstrained is array(natural range <>)       of unsigned;

    **Fix**

    .. code-block:: vhdl

       type t_u_array_unconstrained is array (natural range <>) of unsigned;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.number_of_spaces = 1
