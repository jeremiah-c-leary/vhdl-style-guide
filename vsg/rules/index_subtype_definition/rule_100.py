# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_before_token import Rule

lTokens = []
lTokens.append(token.index_subtype_definition.range_keyword)


class rule_100(Rule):
    """
    This rule checks for a single space before the **range** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       type my_array is array (natural     range <>) of integer;

    **Fix**

    .. code-block:: vhdl

       type my_array is array (natural range <>) of integer;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.number_of_spaces = 1
