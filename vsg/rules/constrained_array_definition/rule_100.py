# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_after_token import Rule

lTokens = []
lTokens.append(token.constrained_array_definition.array_keyword)


class rule_100(Rule):
    """
    This rule checks for whitespace after the **array** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       type t_u_array is array (1 downto 0) of unsigned;
       type t_u_array is array     (1 downto 0) of unsigned;

    **Fix**

    .. code-block:: vhdl

       type t_u_array is array(1 downto 0) of unsigned;
       type t_u_array is array(1 downto 0) of unsigned;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.number_of_spaces = 0
